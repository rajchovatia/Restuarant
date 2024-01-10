from django.db import models

# Create your models here.

class About(models.Model) :
    about_pic1 = models.ImageField(upload_to="about_pic")
    about_pic2 = models.ImageField(upload_to="about_pic")
    about_pic3 = models.ImageField(upload_to="about_pic")
    about_pic4 = models.ImageField(upload_to="about_pic")
    

class Aboutteam(models.Model) :
    about_pic = models.ImageField(upload_to="team_pic")
    about_name = models.CharField()
    about_info = models.CharField()
    about_time = models.CharField()