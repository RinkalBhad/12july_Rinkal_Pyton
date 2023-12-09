from django.shortcuts import render,redirect
from.forms import*
from .models import* 

# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=usersignup.objects.filter(username=unm,password=pas)
        if user:
            print("login successfully")
            return redirect('other')
        else:
            print("invalid username or passwrod")
    return render(request,'index.html')


def signup(request):
     if request.method=='POST':
        user=sign(request.POST)
        if user.is_valid():
            user.save()
            print("saved")
        else:
            print(user.errors)

     return render(request,'signup.html')

def other(request):
    return render(request,'other.html')
