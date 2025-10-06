from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)

# admin.py
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id","user","service","pet_name","pet_type","breed","date","time_slot","status","created_at")
    list_filter = ("service","status","date")
    search_fields = ("pet_name","user__email","breed")
