from django.shortcuts import render
from django.http import HttpResponse
from .models import info
from account.models import booked_flights

def index(request):
    flights = info.objects.all()
    return render(request,'index.html',{
        'info':{'page':'home'} ,
        'flights':flights
    })

def book(request,id):
    currentFlight = info.objects.get(id=id)
    if currentFlight.seats == 0:
        return render(request, 'index.html' , {
            'current':currentFlight ,
            'info':{'page':'confirm-booking'} ,
            'bookingStatus':'Sorry ! No seats left !'
        })
    else:
        currentFlight.seats -= 1
        if booked_flights.objects.filter(user_id=request.user , flight_id = currentFlight).exists():
            return render(request, 'index.html' , {
                'current':currentFlight ,
                'info':{'page':'confirm-booking'} ,
                'bookingStatus':'Sorry ! You can book this flight only once .'
            })
        else:
            bookedFlight = booked_flights(user_id=request.user , flight_id = currentFlight)
            currentFlight.save()
            bookedFlight.save()
            return render(request, 'index.html' , {
                'current':currentFlight ,
                'info':{'page':'confirm-booking'} ,
                'bookingStatus':'Thankyou for booking . Your flight details are as follows :'
            })

def test(request):
    val1= int(request.GET['num1'])
    val2= int(request.GET['num2'])
    res = val1+val2
    return render(request,'test.html', {'result':res})