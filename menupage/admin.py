from django.contrib import admin
from menupage.models import BreakfastMenu,LanchMenu,DinnerMenu
# Register your models here.

class menuadmin(admin.ModelAdmin) :
    list_display = ('breakfast_pic','breakfast_name','breakfast_info','breakfast_price')

admin.site.register(BreakfastMenu,menuadmin)

class lanchadmin(admin.ModelAdmin) :
    list_display = ('lanch_pic','lanch_name','lanch_info','lanch_price')

admin.site.register(LanchMenu,lanchadmin)

class dinneradmin(admin.ModelAdmin) :
    list_display = ('dinner_pic','dinner_name','dinner_info','dinner_price')

admin.site.register(DinnerMenu,dinneradmin)