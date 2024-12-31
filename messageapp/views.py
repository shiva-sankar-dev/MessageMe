from django.shortcuts import render,redirect
from .models import *


# Create your views here.
def room(request):
    if request.method == 'POST':
        username = request.POST['username']
        room = request.POST['room']
        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room.objects.create(room_name=room)
            new_room.save()
        return redirect("message",room_name=room,username=username)
            
    return render(request,"index.html")

def message(request, room_name, username):
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)
    context = {
        "room_name":room_name,
        "user":username,
        "messages": get_messages,
    }
    return render(request,"message.html",context)

def main(request):
    return render(request,"main.html")