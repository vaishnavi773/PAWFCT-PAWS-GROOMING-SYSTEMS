import json
import datetime
from datetime import datetime as dt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.conf import settings

import razorpay
from adminstration.models import serviceDB
from .models import Booking, CustomUser, registrationdb


# Razorpay Client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
User = get_user_model()

# 🏠 Home
def indexpage(request):
    services = serviceDB.objects.all()
    return render(request, "indexfront.html", {"services": services})


# 🟢 Register
def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")

        if password != re_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        user = CustomUser.objects.create_user(email=email, name=name, password=password)
        messages.success(request, "Registration successful! Please login.")
        return redirect("user_login_page")

    return render(request, "register.html")


# 🟢 Login
def user_login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Please provide both email and password")
            return redirect('user_login_page')

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            messages.success(request, f"Welcome, {user.name}!")
            return redirect('indexpage')
        else:
            messages.error(request, "Invalid email or password")
            return redirect('user_login_page')

    return render(request, "login.html")


# 🟢 Logout
def userlogout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("indexpage")


# 🟠 Checkout Page (for Razorpay test mode)
def checkout(request, service_id):
    service = get_object_or_404(serviceDB, id=service_id)
    amount_in_paise = int(service.price * 100)

    order_data = {
        "amount": amount_in_paise,
        "currency": "INR",
        "payment_capture": 1,
        "receipt": f"receipt_{service.id}"
    }

    order = razorpay_client.order.create(order_data)

    return render(request, "checkout_plan.html", {
        "plan": service.servicename,
        "amount": amount_in_paise,
        "order_id": order["id"],
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "service_id": service.id
    })


@login_required(login_url='user_login_page')
@require_POST
def save_booking(request, service_id):
    """Save booking details when user clicks Pay button"""
    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        return JsonResponse({"success": False, "error": "Invalid JSON"}, status=400)

    service = get_object_or_404(serviceDB, id=service_id)

    pet_name = data.get("pet_name")
    pet_type = data.get("pet_type")
    breed = data.get("breed")
    gender = data.get("gender")
    age = data.get("age")
    date_str = data.get("date")
    time_slot = data.get("time_slot")

    if not (pet_name and date_str and time_slot):
        return JsonResponse({"success": False, "error": "Missing required fields"}, status=400)

    try:
        date_obj = dt.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({"success": False, "error": "Invalid date format"}, status=400)

    # 🚫 Prevent booking same slot (any user, not just same user)
    if Booking.objects.filter(service=service, date=date_obj, time_slot__iexact=time_slot).exists():
        return JsonResponse({"success": False, "error": "Slot already booked!"}, status=400)

    # ✅ Save booking
    Booking.objects.create(
        user=request.user,
        service=service,
        pet_name=pet_name,
        pet_type=pet_type,
        breed=breed,
        gender=gender,
        age=age,
        date=date_obj,
        time_slot=time_slot.strip().upper(),
        status="Confirmed"
    )

    # Return updated booked slots for that date
    booked_slots = Booking.objects.filter(service=service, date=date_obj).values_list("time_slot", flat=True)
    return JsonResponse({
        "success": True,
        "slots": [s.strip().upper() for s in booked_slots]
    })


# 🔵 Payment Success Page (optional)
@csrf_exempt
def payment_success(request):
    return render(request, "payment_success.html")


# 🔴 Payment Failed Page
@csrf_exempt
def payment_failed(request):
    return render(request, "payment_failed.html")


# 🟣 About Page
def about(request):
    return render(request, "about.html")


# 🟢 Contact Page
def contact(request):
    return render(request, "contact.html")


# 🟤 Service Listing
def service(request):
    services = serviceDB.objects.all()
    return render(request, "service.html", {"services": services})


# 🟡 Pricing
def price(request):
    return render(request, "price.html")


# ✅ My Bookings
@login_required(login_url='user_login_page')
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "my_bookings.html", {"bookings": bookings})



# ✅ Pet Form (Booking Page)
@login_required(login_url='user_login_page')
def pet(request, service_id):
    user = request.user
    service = get_object_or_404(serviceDB, id=service_id)

    booked_slots = Booking.objects.filter(service=service).values_list('time_slot', flat=True)
    booked_slots_json = json.dumps(list(booked_slots))

    context = {
        "username": request.user.name if hasattr(request.user, "name") else request.user.email,
        "service_name": service.servicename,
        "service_price": service.price,
        "service_id": service.id,
        "booked_slots_json": booked_slots_json,
        "today": date.today().isoformat(),
    }

    return render(request, "pet.html", context)


# 🧾 Register (old fallback)
def saveuser(request):
    if request.method == "POST":
        a = request.POST.get('sname')
        b = request.POST.get('semail')
        c = request.POST.get('password')
        registrationdb.objects.create(name=a, email=b, password=c)
        return redirect(user_login_page)
    
from datetime import date

@login_required(login_url='user_login_page')
def booked_slots(request, service_id):
    """Return JSON of booked slots for a given service and date (for all users)"""
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({"slots": []})

    try:
        date_obj = dt.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return JsonResponse({"slots": []})

    # Get all booked slots for that date, regardless of user
    bookings = Booking.objects.filter(service_id=service_id, date=date_obj)
    slots = list(bookings.values_list('time_slot', flat=True))
    
    # Normalize slots to prevent comparison issues
    slots = [s.strip().upper() for s in slots]

    return JsonResponse({"slots": slots})

