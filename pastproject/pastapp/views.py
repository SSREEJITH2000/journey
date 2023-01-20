from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import venue
from .models import doc
from .models import team

# Create your views here.
def blast(request):
    result=venue.objects.all()
    val=doc.objects.all()
    want=team.objects.all()
    return render(request,'index.html',{'value':result,
                                        'res':val,
                                        'take':want})
def register(request):

    if request.method=='POST':
        use=request.POST['user']
        email=request.POST['mail']
        mobile = request.POST['mob no.']
        usern = request.POST['user_name']
        past = request.POST['pass_word']
        pasts = request.POST['confirm']
        if past==pasts:
            if User.objects.filter(username=usern).exists():
                messages.info(request,'Username taken')
                return redirect('/reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'mail id accepted')
                return redirect('/reg')
            else:
                user=User.objects.create_user(username=usern,first_name=use,email=email,password=past)
                user.save()

        else:
            messages.info(request,'password not matching')
            return redirect('/reg')
        return redirect('/')
    return render(request,'page.html')