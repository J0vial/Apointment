from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class additionalUserInfo(models.Model):
    cat = (
        ('Patient','Patient'),
        ('Hospital_admin','Hospital_admin'),
        
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    catagory = models.CharField(choices=cat,max_length=50)
    phone_no = models.CharField(max_length=11)
    
    status = models.CharField(choices = (('Registerd','Registerd'),('Unregisterd','Unregisterd')),max_length=100,default='Unregisterd')
    hospital_name = models.CharField(max_length=100,null=True)
    
    
    def __str__(self):
        return self.user.username
    
    
