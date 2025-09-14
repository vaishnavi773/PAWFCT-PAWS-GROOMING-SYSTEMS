from django.core.checks import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError

from adminstration.models import serviceDB


# Create your views here.
def home_view(request):
    return render(request,'index.html')
def add_service(request):
    return render(request, "add service.html")
def save_ser(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('description')
        c = request.FILES['image']
        obj = serviceDB(servicename=a, description=b, image=c)
        obj.save()
        messages.success(request,"Service saved sucessfully")
        return redirect(add_service)
def display_ser(request):
    ser = serviceDB.objects.all()
    return render(request, "display_service.html",{'ser':ser})

def edit_ser(request, ser_id):
    ser = serviceDB.objects.get(id=ser_id)
    return render(request, "edit_service.html", {'ser': ser})
def update_ser(request, ser_id):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('description')
        try:
            c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(c.name, c)
        except MultiValueDictKeyError:
            file = serviceDB.objects.get(id=ser_id).image
        serviceDB.objects.filter(id=ser_id).update(servicename=a, description=b, image=file)
        return redirect(display_ser)

def delete_ser(request, ser_id):
    ser =serviceDB.objects.filter(id=ser_id)
    ser.delete()
    messages.success(request, "Deleted sucessfully")
    return redirect(display_ser)