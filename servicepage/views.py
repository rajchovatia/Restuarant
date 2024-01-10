from django.shortcuts import render
from servicepage.models import Service
# Create your views here.

def servicepages(request) :
    servicedata = Service.objects.all()
    data = {'service' : servicedata}
    
    return render(request,"service.html",data)
