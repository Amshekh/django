"""Amshekh_labs_pvt_ltd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Amshekh_labs_pvt_ltd import views # Syntax: from project/website name   then  import  views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first-django-webpage', views.first_django_webpage),
    path('', views.homePage,name='home'), # we leave blank, because we want home page to open directly as user visits website
    path('about-us/', views.aboutUs, name='aboutUs'),
    path('contact-us/', views.contactUs, name='contact'),
    path('userForm/', views.userForm),
    path('submitForm/', views.submitForm, name='submitForm'),
    path('thank-you/', views.thankYou),
    path('calculator/', views.calculator),
    path('evenodd/', views.evenodd),
    path('marksheet/', views.marksheet),
    path('order-a-software/', views.custom_Software_Order, name='softwareProducts')
]
