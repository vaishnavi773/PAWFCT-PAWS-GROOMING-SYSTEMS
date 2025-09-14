from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

# 🏠 Home View
def indexpage(request):
    return render(request, "indexfront.html")

# 🟢 Register View
def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")

        if password != re_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        # ✅ Pass name properly into create_user
        user = User.objects.create_user(email=email, name=name, password=password)

        messages.success(request, "Registration successful! Please login.")
        return redirect("login")

    return render(request, "register.html")


# 🟢 Login View
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # ✅ authenticate with email (USERNAME_FIELD is "email" in CustomUser)
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # redirect to home after login
        else:
            messages.error(request, "Invalid email or password")
            return redirect("login")

    return render(request, "login.html")


# 🟢 Logout View
def logout_view(request):
    logout(request)
    return redirect("home")  # Redirect to home after logout
