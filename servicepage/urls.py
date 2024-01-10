
from django.contrib import admin
from django.urls import path
from servicepage import views

urlpatterns = [
    path('', views.servicepages , name="service"),
]