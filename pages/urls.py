from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('about/ourteam/', views.ourteampage , name="ourteam"),
    path('about/testimonial/', views.testimonialpage , name="testimonial"),
    path('about/booking/', views.bookingpage , name="booking"),
]


urlpatterns += staticfiles_urlpatterns()