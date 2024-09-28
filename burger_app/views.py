from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Hamburger, Subscriber, MenuHamburger, Contact, MenuFries, MenuDrink
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    burgers = Hamburger.objects.all()
    context = {"burger": burgers}
    return render(request, "burger_app/index.html", context=context)

def about(request):
    return render(request, "burger_app/about.html")

def our_food(request):
    burgers = MenuHamburger.objects.all()
    fries = MenuFries.objects.all()
    drinks = MenuDrink.objects.all()
    offers = Hamburger.objects.all()
    context = {"burger": burgers, "fries": fries, "drinks": drinks, "offers": offers}

    return render(request, "burger_app/food.html", context=context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        
        return redirect(f'/contact/?message=success')
    return render(request, "burger_app/contact.html", context={"message": "False"})

@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')

        if email:
            
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                return JsonResponse({'message': 'Thank you for subscribing!'})
            else:
                return JsonResponse({'message': 'This email is already subscribed.'})
        return JsonResponse({'message': 'Invalid email.'}, status=400)
    
    return JsonResponse({'message': 'Method not allowed.'}, status=405)
