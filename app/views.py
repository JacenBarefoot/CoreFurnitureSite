from django.shortcuts import render
from app.models import *
    
def home(request):
    context = {
        "contract_info": Contract_info.objects.first()
    }
    return render(request, 'index.html', context)
    
def browse(request):
    context = {
        "footer": Footer.objects.first()
    }
    return render(request, 'browse.html', context)
    
def hometest(request):
    return render(request, 'hometest.html')

def hometest2(request):
    return render(request, 'hometest2.html')
    
def about(request):
    context = {
        "about": About.objects.first(),
        "footer": Footer.objects.first()
    }
    return render(request, 'about.html', context)

def categories(request, category):
    context = {
        "category": category,
        "content": Item.objects.filter(type=category),
        "footer": Footer.objects.first()
    }
    return render(request, 'items.html', context)

def testimonies(request):
    context = {
        "testimonies": Testimony.objects.all(),
        "footer": Footer.objects.first()
    }
    return render(request, 'Testimonies.html', context)
