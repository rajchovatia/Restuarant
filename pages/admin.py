from django.contrib import admin
from pages.models import TestiMonial,Booking
# Register your models here.

# class teamadmin(admin.ModelAdmin) :
#     list_display = ('team_pic','team_name','team_info','team_time')

# admin.site.register(OurTeam,teamadmin)

class testimonialadmin(admin.ModelAdmin) :
    testimonial_list = ('testimonial_pic','testimonial_name','testimonial_about','testimonial_dis')

admin.site.register(TestiMonial,testimonialadmin)

class bookingadmin(admin.ModelAdmin) :
    booking_info = ('costomername','costomeremail','DateTime','totalpeople','special_request')
    
admin.site.register(Booking,bookingadmin)