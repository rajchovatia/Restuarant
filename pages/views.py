from django.shortcuts import render,redirect
from pages.models import TestiMonial
# Create your views here.
from pages.models import Booking
from datetime import datetime

from aboutpage.models import About,Aboutteam
def ourteampage(request) :
    aboutteamdata = Aboutteam.objects.all()
    data = {'ourteam' : aboutteamdata}
    
    return render(request,"ourteam.html",data) 


def testimonialpage(request) :
        testimonialdata = TestiMonial.objects.all()
    
        print(testimonialdata)
        data = {'testimonialdata' : testimonialdata} 
        
        return render(request,"testimonial.html",data)
    
def bookingpage(request) :
    if request.method == "POST" :
        costomername = request.POST.get('name')
        costomeremail = request.POST.get('email') 
        DateTime = request.POST.get('datetime')
        totalpeople = request.POST.get('select1')
        special_request = request.POST.get('message')
    
        DateTime = datetime.strptime(DateTime, "%d/%m/%Y %H:%M %p")            
        print(costomername,costomeremail,DateTime,totalpeople,special_request)
        
        bookingdata = Booking(costomername=costomername,costomeremail=costomeremail,DateTime=DateTime,totalpeople=totalpeople,special_request=special_request)
        bookingdata.save()
        
        return redirect('/')
    
    return render(request,"booking.html")