from django.shortcuts import render
from app.models import Item

def home3(request):
    return render(request, 'Home3.html')

def itemPage(request):
    return render(request, 'ItemPage.html')
    
def homeTest(request):
    return render(request, 'Home4.html')
    
def browseTest(request):
    context = {
        'products': Item.objects.all()
    }
    return render(request, 'BrowseTest.html', context)
    
def about(request):
    return render(request, 'About.html')

def itemEntry(request, id):
    context = {
        "id": id,
        "items": Item.objects.all()
    }
    return render(request, "itemEntry.html", context)