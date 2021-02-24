from django.shortcuts import render , redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from .forms import UpdateUserForm
from .models import booked_flights

# Create your views here.
def register(request):
    info = {'page':'register'}

    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('/account/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('/account/register')
            else:
                user = User.objects.create_user(username=username , password=password1 , email=email , first_name=fname , last_name= lname )
                user.save()
                print("user created")
                return redirect('/account/login')
        else:
            messages.info(request,'Passwords dont match')
            return redirect('/account/register')
    else:
        return render(request, 'index.html' , {'info':info})

def login(request):
    info = {'page':'login'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/account/login')
    else:
        return render(request, 'index.html' , {'info':info})


def logout(request):
    auth.logout(request)
    return redirect('/')

def update_user(request,id=0):
    
    if request.method == 'POST': 
        user = User.objects.get(id=id)
        form = UpdateUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Saved Changes Successfully ')
        return redirect('/account/'+str(id))
    else:
        user = User.objects.get(id=id)
        form = UpdateUserForm(instance=user)
        bookedFlight = booked_flights.objects.filter(user_id=request.user.id)
        context = {'form':form}
        info = {'page':'profile'}
        return render(request, 'index.html', {
            'context':context ,
            'info':info,
            'booked':bookedFlight
            })