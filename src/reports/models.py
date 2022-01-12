from django.db import models
from profiles.models import Profile

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=120)
    #to store charts
    image = models.ImageField(upload_to='reports', blank=True)
    #to store thoughts based on charts
    remarks = models.TextField()
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)    #foreign key from profiles model
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

        