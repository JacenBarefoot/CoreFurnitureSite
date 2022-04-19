from django.shortcuts import render
from app.models import Item

def home3(request):
    products = Item.objects.all()
    context = {'products': products}
    return render(request, 'Home3.html', context)

def itemPage(request):
    return render(request, 'ItemPage.html')
    
def homeTest(request):
    return render(request, 'Home4.html')
    
def about():
    ...

def itemEntry(request, id):
    context = {
        "id": id,
        "items": Item.objects.all()
    }
    return render(request, "itemEntry.html", context)