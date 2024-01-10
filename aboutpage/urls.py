from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path
from aboutpage import views

urlpatterns = [
    path('', views.aboutpage , name="about"),  
    path('aboutadd/', views.aboutadd , name="aboutadd"),
]

urlpatterns += staticfiles_urlpatterns()
