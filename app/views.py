from django.shortcuts import render
from app.models import Item, About, Testimony
    
def home(request):
    return render(request, 'index.html')
    
def browse(request):
    return render(request, 'browse.html')
    
def hometest(request):
    return render(request, 'hometest.html')

def hometest2(request):
    return render(request, 'hometest2.html')
    
def about(request):
    context = {
        "about": About.objects.all()
    }
    return render(request, 'about.html', context)

def categories(request, category):
    context = {
        "category": category,
        "content": Item.objects.filter(type=category)
    }
    return render(request, 'items.html', context)

def testimonies(request):
    context = {
        "testimonies": Testimony.objects.all()
    }
    return render(request, 'Testimonies.html', context)
