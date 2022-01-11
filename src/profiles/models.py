from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #when the user is deleted, the profile will also be deleted.
    bio = models.TextField(default="no bio")
    avatar = models.ImageField(upload_to='avatars', default='no_img.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return f"Profile of {self.user.username}"