from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def login(request):
    c={}
    c.update(csrf(request))
    return render(request,'login.html',c)

def auth_user(request):
    username=request.POST.get('subject','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/loggedin/')
    else:
        return HttpResponseRedirect('/invalid/')

def loggedin(request):
    username=auth.get_user(request).username
    return render(request,'loggedin.html',
        {'username':username})

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')

def invalid(request):
    return render(request,'invalid_login.html')

def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/register_success/')
    args={}
    args.update(csrf(request))
    args['form']=UserCreationForm()
    return render(request,'register_user.html',args)

def register_success(request):
    return render(request,'register_success.html')
