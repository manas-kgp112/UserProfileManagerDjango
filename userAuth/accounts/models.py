from email.policy import default
from django.db import models
from django import forms
from django.contrib.auth.models import User



# Create your models here.


class authUser(models.Model):
    MEET = (
        ('G-Meet','G-Meet'),
        ('Ms-Teams','Ms-Teams'),
        ('Offline','Offline'),
        ('Zoom','Zoom')
    )
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    date_created = models.DateField(null=True, auto_now_add=True, blank=True)
    meet = models.CharField(null=True, max_length=500, choices=MEET, blank=True)
    image = models.ImageField(null=True, blank=True, default='2566555.jpg')


    def __str__(self) -> None:
        return self.name
