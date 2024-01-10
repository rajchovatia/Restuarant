from django.shortcuts import render,redirect

# Create your views here.
from contactpage.models import ContactDetails

def contactpage(request) :
    if request.method == "POST" :
        username = request.POST.get('name')
        useremail = request.POST.get('email')
        usersubject = request.POST.get('subject')
        usermessage = request.POST.get('message')
        
        # print(username,useremail,usersubject,usermessage)
        
        userdata = ContactDetails(username=username,useremail=useremail,usersubject=usersubject,usermessage=usermessage)
        userdata.save()
        return redirect('/')
    
    return render(request,"contact.html")