from django.shortcuts import render,redirect
from django.http import HttpResponse
from aboutpage.models import About,Aboutteam
# Create your views here.
from django.contrib.auth.decorators import login_required

def aboutpage(request) :
    aboutdata = About.objects.all()
    aboutteamdata = Aboutteam.objects.all()
    
    data = {'about' : aboutdata,
            'aboutteam' : aboutteamdata}
    
    return render(request,"about.html", data)

@login_required(login_url='login')
def aboutadd(request) :
        if request.method == "POST" :
                aboutname = request.POST.get('name')
                img_bio = request.POST.get('userinfo')
                slice_time = request.POST.get('time')
                picture = request.POST.get('myfile')
                
                print(aboutname,img_bio,slice_time,picture)
                teamdata = Aboutteam(about_pic=picture,
                                about_name=aboutname,
                                about_info=img_bio,
                                about_time=slice_time)
                
                teamdata.save()
                print("data insert successfully !")
                return redirect('about')
        return render(request,"template_about/about_teampic_add.html")