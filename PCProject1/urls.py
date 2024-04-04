"""PCProject1 URL Configuration

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
from django.urls import path,re_path
from MyApps1 import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Homepage/', views.homepage_view),
    path('Aboutus/', views.aboutus_view),
    path('Australia/', views.australia_view),
    path('Canada/', views.canada_view),
    path('Contactus/', views.contactus_view),
    path('France/', views.france_view),
    path('Germany/', views.germany_view),
    path('India/', views.india_view),
    path('UAE/', views.uae_view),
    path('UK/', views.uk_view),
    path('USA/', views.usa_view),
    path('homepage/',views.contactus_view),
    path('homepage/', views.common_css_view),
    path('contact us/', views.contactus_css_view),
]
