from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.http import JsonResponse

# Create your views here.
def room(request):
    user = request.user
    if request.method == 'POST':
        # username = request.POST['username']
        room = request.POST['room']
        try:
            get_room = Room.objects.get(room_name=room)
        except Room.DoesNotExist:
            new_room = Room.objects.create(room_name=room)
            new_room.save()
        return redirect("message",room_name=room,username=user)
            
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

def loginpage(request):
    if request.method == "POST":
        username = request.POST["log_username"]
        log_password = request.POST["log_password"]
        print("Username:", username)
        user = authenticate(request, username=username,password = log_password)
        if user is not None:
            login(request,user)
            return redirect("room")
    return render(request,"loginpage.html")

def registration(request):
    if request.method == 'POST':
        username = request.POST["reg_username"]
        email = request.POST.get("reg_email")
        profile_picture = request.FILES.get("reg_profile_picture")
        password = request.POST.get("reg_password")
        print("Username:", username)
        print("Email:", email)
        print("Profile Picture:", profile_picture)
        print("Password:", password)
        if User.objects.filter(username = email).exists():
            messages.error(request, "email already exist")
            print("email already exist")
        else:
            user_reg = User.objects.create_user(username=email,email=email)
            user_reg.set_password(password)
            user_reg.first_name = username
            user_reg.save()
            Profile.objects.create(user=user_reg,profile_picture=profile_picture)
            return JsonResponse({"added":True})
    
    return render(request,"loginpage.html")

def logout_page(request):
    return render(request,"loginpage.html")
