from django.db import models

# Create your models here.

# class OurTeam(models.Model) :
#     team_pic = models.ImageField(upload_to="Team_picture")
#     team_name = models.CharField(max_length=100)
#     team_info = models.CharField(max_length=100)
#     team_time = models.CharField(max_length=100)
    

class TestiMonial(models.Model) :
    testimonial_pic = models.ImageField(upload_to="Testimonial_picture")
    testimonial_name = models.CharField(max_length=100)
    testimonial_about = models.CharField(max_length=100)
    testimonial_dis = models.TextField()
    

class Booking(models.Model) :
    costomername = models.CharField(max_length=200)
    costomeremail = models.EmailField(max_length=100,blank=False,unique=True)
    DateTime = models.DateTimeField()
    totalpeople = models.IntegerField()
    special_request = models.TextField()
    
    