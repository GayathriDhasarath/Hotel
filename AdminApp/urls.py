
from django.urls import path
from .import views

urlpatterns = [
    path('',views.AddHotel,name='AddHotel'),
    path('viewhotel/',views.ViewHotel,name='ViewHotel'),
    path('hotel/',views.hotel,name='hotel'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('adminindex/',views.adminindex,name='adminindex'),
    path('sample/',views.sample,name='sample'),
    path('demo/',views.demo,name='demo'),
    path('travel/',views.travel,name='travel'),
    path('travel_table/',views.travel_table,name='travel_table'),
    path('datas/',views.datas,name='datas'),
    path('travel_edit/<int:id>/',views.travel_edit,name='travel_edit'),
    path('travel_update/<int:id>/',views.travel_update,name='travel_update'),
    path('Travel_mod/',views.Travel_mod,name='Travel_mod'),
    path('travel_delete/<int:id>/',views.travel_delete,name='travel_delete'),
    path('user_message/',views.user_message,name='user_message'),
    path('userdetails_delete/<int:id>/',views.userdetails_delete,name='userdetails_delete')

]
