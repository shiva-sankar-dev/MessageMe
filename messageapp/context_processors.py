from .models import *


def userprofile(request):
    viewusername ="" 
    dp ="" 
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return {"dp": "", "viewusername": ""}
        get_user = Profile.objects.get(user = request.user)
        get_user_name = User.objects.get(username = request.user)
        if get_user.profile_picture:
            dp = get_user.profile_picture
        else:
            pass
        viewusername = get_user_name.first_name
    context ={
        "dp":dp,
        "viewusername":viewusername,
    }
    return context