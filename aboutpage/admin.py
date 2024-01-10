from django.contrib import admin
from aboutpage.models import About,Aboutteam

# Register your models here.

class aboutadmin(admin.ModelAdmin) :
    list_display = ('about_pic1','about_pic2','about_pic3','about_pic4')
    
admin.site.register(About,aboutadmin)


class aboutteam(admin.ModelAdmin) :
    list_aboutteam = ('about_pic','about_name','about_info')

admin.site.register(Aboutteam,aboutteam)