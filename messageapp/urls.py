from django.urls import path
from .views import *

urlpatterns = [
    path('messge/<str:room_name>/<str:username>/',message,name="message" ), 
    path('room',room,name="room" ), 
    path('main/',main,name="main" ), 
    path('loginpage/',loginpage,name="loginpage" ), 
    path('',registration,name="registration" ), 
    path('logout_page/',logout_page,name="logout_page" ), 
]

from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)