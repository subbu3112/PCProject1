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
    path('homepage/', views.homepage_view),
    path('aboutus/', views.aboutus_view),
    path('australia/', views.australia_view),
    path('canada/', views.canada_view),
    path('contactus/', views.contactus_view),
    path('france/', views.france_view),
    path('germany/', views.germany_view),
    path('india/', views.india_view),
    path('uae/', views.uae_view),
    path('uk/', views.uk_view),
    path('usa/', views.usa_view),
    path('homepage/',views.contactus_view),
    path('homepage/', views.common_css_view),
    path('contact us/', views.contactus_css_view),
]
