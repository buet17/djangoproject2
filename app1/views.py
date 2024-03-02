from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from app1 import views

# Create your views here.

def index(request):
    # template_name=loader.get_template('index.html')
    # return HttpResponse(template_name.render())

    listStd=[
        {
            'name':'Mr. Shakhawat',
            'age':22,
            'id':170220240011
        },
        {
            'name':'Mr. Rahim',
            'age':24,
            'id':170220240012
        },
        {
            'name':'Mr. Karim',
            'age':21,
            'id':170220240013
        },
    ]
    # total_age=0
    # std_no=len(listStd)

    # for x in listStd:
    #     total_age=total_age+x['age']
    # avg_age1=total_age/std_no
    # print(avg_age1)
    return render(request, 'index.html',{'students':listStd})
    # return render(request, 'index.html',{'AVG':avg_age1})


def about(request):
    template_name=loader.get_template('about.html')
    return HttpResponse(template_name.render())
    # return render(request, 'about.html')

def contact(request):
    name="Md Noor Alam"
    return render(request,'contact.html',{'name':name})
    # return render(request, 'contact.html')

def services(request):
    # template_name=loader.get_template('index.html')
    # return HttpResponse(template_name.render())

    listStd=[
        {
            'name':'Mr. Shakhawat',
            'age':22,
            'id':170220240011
        },
        {
            'name':'Mr. Rahim',
            'age':24,
            'id':170220240012
        },
        {
            'name':'Mr. Karim',
            'age':21,
            'id':170220240013
        },
    ]
    total_age=0
    std_no=len(listStd)

    for x in listStd:
        total_age=total_age+x['age']
    avg_age1=total_age/std_no
    # print(avg_age1)
    return render(request, 'services.html',{'AVG':avg_age1})
    # return render(request, 'index.html',{'AVG':avg_age1})

# Routing ustom_404 view error handing
def custom_404(request,exception):
    return render(request, '404.html', status=404)
    # return redirect('home')

# Internal codding error is called 500 error
def custom_500(request):
    return render(request, '500.html', status=500)
    # return redirect('home')





