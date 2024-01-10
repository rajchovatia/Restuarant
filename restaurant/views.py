from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages 


def homepage(request) :
    return render(request,"index.html")


def loginpage(request) :
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        print("complete !!!!!")
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username !!")
            return redirect('/loginpage/')
        
        user = authenticate(username=username,password=password)
        if user is None :
            messages.error(request,"Invalid Password !")
            return redirect('login')
        else :
            login(request,user)
            return redirect('menuadd')
        
    return render(request,"login_page.html")


def logoutpage(request) :
    logout(request)
    return redirect('/')




