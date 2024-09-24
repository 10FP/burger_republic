from django.shortcuts import render
from .models import Hamburger

# Create your views here.
def index(request):
    burgers = Hamburger.objects.all()
    context = {"burger": burgers}
    return render(request, "burger_app/index.html", context=context)

def about(request):
    return render(request, "burger_app/about.html")

def our_food(request):
    return render(request, "burger_app/food.html")

def contact(request):
    return render(request, "burger_app/contact.html")

def menu(request):
    burgers = Hamburger.objects.all()
    context = {"burger": burgers}
    return render(request, "burger_app/menu.html", context=context)
