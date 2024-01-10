from django.db import models

# Create your models here.

class ContactDetails(models.Model) :
    username = models.CharField(max_length=255)
    useremail = models.EmailField(max_length=70,blank=True,unique=True)
    usersubject = models.CharField(max_length=255)
    usermessage = models.TextField()
    