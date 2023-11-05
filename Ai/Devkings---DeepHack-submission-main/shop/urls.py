from django.contrib import admin
from django.urls import path
from . import views
from shop import views
urlpatterns = [



path('',views.SignupPage,name='signup'),
 path('login/',views.LoginPage,name='login'),
path('logout/',views.LogoutPage,name='logout'),






    
]

