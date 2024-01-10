from django.shortcuts import render,redirect
from menupage.models import BreakfastMenu,LanchMenu,DinnerMenu
# Create your views here.
from django.contrib.auth.decorators import login_required

def menupage(request) :
    breakfastdata = BreakfastMenu.objects.all()
    lanchdata = LanchMenu.objects.all()
    dinnerdata = DinnerMenu.objects.all()
    
    data = {'breakfastmenu' : breakfastdata,
            'lanchmenu' : lanchdata ,
            'dinnermenu' : dinnerdata}
    
    return render(request,"menu.html",data)


@login_required(login_url='login')
def menuadd(request) :
        if request.method == "POST" :
                foodlist = request.POST.get('foodlist')
                picture = request.FILES['picture']
                # picture = request.POST.get('picture')
                name = request.POST.get('name')
                infomation = request.POST.get('infomation')
                price = request.POST.get('price')
                
                print(foodlist,picture,name,infomation,price)
                if foodlist == "breakfast" :
                        data = BreakfastMenu(breakfast_pic=picture,
                                                breakfast_name=name,
                                                breakfast_info=infomation,
                                                breakfast_price=price)
                        data.save()
                elif foodlist == "lunch" :
                        data = LanchMenu(lunch_pic=picture,
                                        lunch_name=name,
                                        lunch_info=infomation,
                                        lunch_price=price)
                        data.save()
                        
                elif foodlist == "dinner" :
                        data = DinnerMenu(dinner_pic=picture,
                                        dinner_name=name,
                                        dinner_info=infomation,
                                        dinner_price=price)
                        data.save()

                print("Data insert successfully !!")
                
                return redirect('menu')
        return render(request,"menu_add/menu_add.html")

