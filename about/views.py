from django.shortcuts import render
from django.http import HttpResponse
from .models import Members

def index(request):
    info = {
        'creators':'Sahil , Vivek and Vikas',
        'prof':'Prof. John Kenny',
        'startingDate':'15-02-21',
        'projectName':'Flight Booking System',
        'course':'SBL-Python',
        'built':'Django',
        'details':'Miniproject Sem 4',
        'page':'about'
    }

    members = Members.objects.all()

    return render(request,'index.html',{'members':members, 'info':info})
    
