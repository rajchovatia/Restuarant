from django.db import models

# Create your models here.

class BreakfastMenu(models.Model) :
    breakfast_pic = models.ImageField(upload_to="menu_picture")
    breakfast_name = models.CharField(max_length=100)
    breakfast_info = models.CharField(max_length=255)
    breakfast_price = models.IntegerField()


class LanchMenu(models.Model) :
    lanch_pic = models.ImageField(upload_to="menu_picture")
    lanch_name = models.CharField(max_length=100)
    lanch_info = models.CharField(max_length=255)
    lanch_price = models.IntegerField()
    

class DinnerMenu(models.Model) :
    dinner_pic = models.ImageField(upload_to="menu_picture")
    dinner_name = models.CharField(max_length=100)
    dinner_info = models.CharField(max_length=255)
    dinner_price = models.IntegerField()