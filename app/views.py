from django.shortcuts import render
from app.models import Item
    
def home(request):
    return render(request, 'index.html')
    
def browse(request):
    return render(request, 'browse.html')
    
def about(request):
    return render(request, 'about.html')

def categories(request, category):
    items = Item.objects.filter(type=category)
    context = {
        'category': category,
        'items': items
    }
    return render(request, 'items.html', context)