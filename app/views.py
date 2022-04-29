from django.shortcuts import render
from app.models import Item, About
    
def home(request):
    return render(request, 'index.html')
    
def browse(request):
    return render(request, 'browse.html')
    
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