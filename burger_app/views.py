from django.shortcuts import render
from .models import Hamburger, Subscriber
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
    return render(request, "burger_app/food.html")

def contact(request):
    return render(request, "burger_app/contact.html")

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
