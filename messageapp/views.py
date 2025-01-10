from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="loginpage")
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
        return redirect("message",room_name=room)
            
    return render(request,"index.html")

@login_required(login_url="loginpage")
def message(request, room_name):
    user = request.user.id
    get_room = Room.objects.get(room_name=room_name)
    get_messages = Message.objects.filter(room=get_room)
    user_profile_picture = Profile.objects.get(user = user)
    dp = user_profile_picture.profile_picture
    context = {
        "room_name":room_name,
        "user":user,
        "dp":dp,
        "messages": get_messages,
    }
    return render(request,"message.html",context)

def main(request):
    return render(request,"main.html")

def loginpage(request):
    if request.method == "POST":
        username = request.POST["log_username"]
        log_password = request.POST["log_password"]
        user = authenticate(request, username=username,password = log_password)
        if user is not None:
            login(request,user) 
            return redirect("room")
        else:
            messages.error(request,"Invalid email or password.")
            return redirect("loginpage")
    return render(request,"loginpage.html")

def registration(request):
    if request.method == 'POST':
        username = request.POST["reg_username"]
        email = request.POST.get("reg_email")
        # profile_picture = request.FILES.get("reg_profile_picture")
        password = request.POST.get("reg_password")
        if User.objects.filter(username = email).exists():
            return JsonResponse({"exists":True,"message":"Email already exist"})
        else:
            user_reg = User.objects.create_user(username=email,email=email)
            user_reg.set_password(password)
            user_reg.first_name = username
            user_reg.save()
            Profile.objects.create(user=user_reg)
            return JsonResponse({"added":True}) 
            # else:
            #     Profile.objects.create(user=user_reg,profile_picture='profile_image/chibi-luffy-one-3840x2160-13063.png')                
            #     return JsonResponse({"added":True})
    
    return render(request,"loginpage.html")

def logout_page(request):
    logout(request)
    return render(request,"loginpage.html")

login_required(login_url="loginpage")
def profile(request):
    if request.user.is_authenticated:   
        
        user_details = Profile.objects.get(user = request.user)
        if request.method == "POST":
            
            update_username = request.POST["update_username"]
            update_email = request.POST["update_email"]
            update_profile_picture = request.FILES.get("update_profile_picture")

            user_details.user.first_name = update_username
            user_details.user.email = update_email
            user_details.user.username = update_email
            user_details.user.save()
            if update_profile_picture:
                user_details.profile_picture = update_profile_picture
                user_details.save()
            
            
            return redirect("profile")
        context = {
            "user_details":user_details,
        }
        
    else:
        return redirect("loginpage")
            

    return render(request,"profile.html",context)
