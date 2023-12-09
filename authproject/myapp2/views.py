from django.shortcuts import render,redirect
from .forms import*
from .models import *
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=peoplesign.objects.filter(username=unm,password=pas)
        if user:
            print("login successfully")
            request.session['user']=unm   #session
            return redirect("home")
            
        else:
            print("invalid username or passwrod")
    return render(request,'index.html')


def signup(request):
    if request.method=='POST':
        user=si(request.POST)
        if user.is_valid():
            user.save()
            print("saved")
            return redirect("home")
        else:
            print(user.errors)
    return render(request,'signup.html')


def home(request):
    user=request.session.get('user')
    return render(request,'home.html',{"user":user})

def userlogout(request):
    logout(request)
    return redirect('/')