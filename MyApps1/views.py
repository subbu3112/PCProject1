from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from  django.views.generic import ListView,CreateView,DeleteView
from django.core.mail import send_mail
#from taggit.models import Tag
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def homepage_view(request):
    return render(request, 'PCAPP/Home.html')

def aboutus_view(request):
    return render(request, 'PCAPP/About US.html')

def australia_view(request):
    return render(request, 'PCAPP/AUSTRALIA.html')

def canada_view(request):
    return render(request, 'PCAPP/CANADA.html')

def contactus_view(request):
    return render(request, 'PCAPP/contact us.html')

def france_view(request):
    return render(request, 'PCAPP/FRANCE.html')

def germany_view(request):
    return render(request, 'PCAPP/GERMANY.html')

def india_view(request):
    return render(request, 'PCAPP/INDIA.html')

def uae_view(request):
    return render(request, 'PCAPP/UAE.html')

def uk_view(request):
    return render(request, 'PCAPP/UK.html')

def usa_view(request):
    return render(request, 'PCAPP/USA.html')

from django.shortcuts import render
from django.http import HttpResponse
def common_css_view(request):
    return render(request, 'PCAPP/Home.html')

def contactus_css_view(request):
    return render(request, 'PCAPP/Home.html')

def index_css_view(request):
    return render(request, 'PCAPP/Home.html')