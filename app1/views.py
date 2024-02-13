from django.shortcuts import render, HttpResponse
from app1 import views

# Create your views here.

def index(request):
    # name="AIB PLC"
    return render(request, 'index.html')
    # return HttpResponse(f"Hello World: {name}")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')



