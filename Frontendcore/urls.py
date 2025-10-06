from django.urls import path
from . import views
from adminstration.views import display_ser
# from django.views.generic import TemplateView

urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('register/', views.register_view, name='register'),
    path('login/', views.user_login_page, name='user_login_page'),
    path('logout/', views.userlogout, name='userlogout'),
    path('service/', views.service, name='service'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('price/', views.price, name='price'),
    path('pet/<int:service_id>/', views.pet, name='pet'),
    path('checkout/<int:service_id>/', views.checkout, name='checkout'),
    path('save-booking/<int:service_id>/', views.save_booking, name='save_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),
   path('booked-slots/<int:service_id>/', views.booked_slots, name='booked_slots'),

]