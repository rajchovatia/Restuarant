from django.contrib import admin
from servicepage.models import Service
# Register your models here.

class serviceadmin(admin.ModelAdmin) :
    list_display = ('service_icon','service_title','service_dis','service_time')

admin.site.register(Service,serviceadmin)