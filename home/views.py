from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
from django.contrib import messages

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('login')
    return render(request,"index.html")
def loginuser(request):
    if request.method=="POST":
        usernamex = request.POST.get('username')
        passwordx = request.POST.get('password')       
        loginx = authenticate(username=usernamex,password=passwordx)
        if loginx is not None:
                 login(request,loginx)
                 return redirect('/')
        else:        
                return render(request,"login.html")
        
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "You have successfully logged out")
    return redirect('login')