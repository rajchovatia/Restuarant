from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
from django.urls import path
from contactpage import views

urlpatterns = [
    path('', views.contactpage , name="contact"),
    
]




urlpatterns += staticfiles_urlpatterns()