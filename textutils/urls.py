from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index , name='index'),
    path('analyze/', views.analyzed , name='analyzed'),
    path('contact/', views.contact , name='Contactus'),
    path('about/', views.about , name='Contactus'),
    path('privacy/', views.privacy , name='PrivacyPolicy'),

]