from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid')
            return redirect('login')
    return render(request,'login.html')
def registration(request):
    if request.method=='POST':
        give = request.POST['first_name']
        gave = request.POST['last_name']
        get = request.POST['mobile']
        got = request.POST['mail']
        buy = request.POST['username']
        pas = request.POST['password']
        conf = request.POST['confirm']
        if pas==conf:
            if User.objects.filter(username=buy).exists():
                messages.info(request,'Username already taken')
                print("User registered")
                return redirect('register')
            elif User.objects.filter(email=got).exists():
                messages.info(request,'email already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=buy,first_name=give,last_name=gave,email=got,password=pas)
                user.save()
                print("User registered")
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return redirect('/')
    return render(request,'indoor.html')
#
def log_out(request):
    auth.logout(request)
    return redirect('/')
