from .models import *


def userprofile(request):
    print("###############################")
    viewusername ="" 
    dp ="" 
    if request.user.is_authenticated:
        get_user = Profile.objects.get(user = request.user)
        print(get_user,"DDDDDDDDDDDDDDDDDDDDDDDDD")
        get_user_name = User.objects.get(username = request.user)
        dp = get_user.profile_picture
        print(dp,"VVVVVVVVVVVVVVVVVVV")
        viewusername = get_user_name.first_name
    context ={
        "dp":dp,
        "viewusername":viewusername,
    }
    return context