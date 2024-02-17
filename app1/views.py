from django.shortcuts import render, HttpResponse
from app1 import views

# Create your views here.

def index(request):
    # name="AIB PLC"
    listStd=[
        {
            'Name':'Mr. Shakhawat',
            'age':22,
            'ID':170220240011
        },
        {
            'Name':'Mr. Rahim',
            'age':24,
            'ID':170220240012
        },
        {
            'Name':'Mr. Karim',
            'age':21,
            'ID':170220240013
        },
    ]
    total_age=0
    std_no=len(listStd)

    for x in listStd:
        total_age=total_age+x['age']
    avg_age1=total_age/std_no
    print(avg_age1)
    return render(request, 'index.html',{'Student':'age'})
    # return HttpResponse(f"Hello World: {name}")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')



