from django.urls import path
from .views import *

urlpatterns = [
    path('messge/<str:room_name>/<str:username>/',message,name="message" ), 
    path('',room,name="room" ), 
    path('main/',main,name="main" ), 
]
