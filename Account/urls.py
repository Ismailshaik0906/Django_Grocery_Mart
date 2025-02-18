from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('register/',Register,name='Register'),
    path('login/',ulogin,name='login'),
    path('profile/',profile,name='profile'),
    path('logout/',ulogout,name='logout'),
    path('update/<int:id>/',update,name='update'),
    path('category/<str:id>/',product_detail,name='product_detail'),
    path('product/<int:id>/',product_info,name='product_info'),
    path('contactus/',contact,name='contact'),
]