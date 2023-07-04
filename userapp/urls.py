
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
  path('userindex/',views.userindex,name='userindex'),
  path('readmore/<int:id>/',views.readmore,name='readmore'),
  path('contact/',views.contact,name='contact'),
  path('contact_details/',views.contact_details,name='contact_details'),
  path('login/',views.login,name='login'),
  path('register/',views.register,name='register'),
  path('register_user/',views.register_user,name='register_user'),
  path('logindata/',views.logindata,name='logindata') ,
  path('logout/',views.logout,name='logout'),
]