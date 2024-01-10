from django.contrib import admin

from contactpage.models import ContactDetails

# Register your models here.

class contactdetailsadmin(admin.ModelAdmin) :
    list_display = ('username','useremail','usersubject','usermessage')
    
admin.site.register(ContactDetails,contactdetailsadmin)
