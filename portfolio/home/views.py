from django.shortcuts import render, HttpResponse
from home import models

# Create your views here.
def home(request):
    context = {'name': 'Ronit', 'course': 'Django'}
    return render(request, 'home.html', context)

def about(request):
    return render(request,'about.html')

def project(request):
    return render(request,'project.html')

def contact(request):
    if request.method=="POST":
        print("This is post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        print(name, email, phone, desc)
        ins = models.Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        print("The data has been commited to the db.")

    return render(request,'contact.html')