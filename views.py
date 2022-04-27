from multiprocessing import context
import re
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context= {
        'var':'jay'
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is home page")

def about(request):
    #return HttpResponse("This is about page")
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        contact = Contact(name= "name", email="email", phone="phone", date= datetime.today())
        contact.save()

        messages.success(request, 'Submitted Sucessfully...')

    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")   