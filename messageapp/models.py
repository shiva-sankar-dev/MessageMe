from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_image',null=True)
    
    def __str__(self):
        return self.user.username


class Room(models.Model):
    room_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.room_name
    
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # sender = models.CharField(max_length=255)
    sender = models.ForeignKey(Profile,on_delete=models.CASCADE)
    message = models.TextField()
    
    def __str__(self):
        return str(self.room)