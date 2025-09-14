from django.urls import path
from adminstration import views
urlpatterns = [
    path('home/',views.home_view,name="home_view"),
path('add_service/',views.add_service,name="add_service"),
path('save_ser/',views.save_ser,name="save_ser"),
path('display_ser/',views.display_ser,name="display_ser"),
path('edit_ser/<int:ser_id>/',views.edit_ser,name="edit_ser"),
path('update_ser/<int:ser_id>/',views.update_ser,name="update_ser"),
path('delete_ser/<int:ser_id>/',views.delete_ser,name="delete_ser"),
]