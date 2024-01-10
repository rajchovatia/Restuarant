from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path
from menupage import views

urlpatterns = [
    path('', views.menupage, name="menu"),
    path('menuadd/', views.menuadd, name="menuadd"),
]


if settings.DEBUG :
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
