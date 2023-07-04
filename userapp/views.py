from django.shortcuts import render,redirect
from .import views
from AdminApp.models import*
from .models import *

# Create your views here.
def userindex(request):
    data=Travel_mod.objects.all()
    return render(request,'userindex.html',{'data':data})
def readmore(request,id):
    data=Travel_mod.objects.filter(id=id)
    return render(request,'singleproduct.html',{'data':data})
def contact(request):
    return render(request,'contact.html')
def contact_details(request):
    name=request.POST['name']
    email=request.POST['email']
    sub=request.POST['sub']
    message=request.POST['message']
    data=Contact_details(name=name,email=email,sub=sub,message=message)
    data.save()
    
    return redirect('userindex')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def register_user(request):
    name=request.POST['name']
    email=request.POST['email']
    contact=request.POST['contact']
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']
    data=User_details(name=name,email=email,contact=contact,password=password,confirm_password=confirm_password)
    data.save()
    return redirect('login')
def logindata(request):
    if request.method=="POST":
        username2=request.POST['name']
        password2=request.POST['password']
        if User_details.objects.filter(name=username2,password=password2).exists():
            data = User_details.objects.filter(name=username2,password=password2).values('email','contact','id').first()
            
            request.session['uemail'] = data['email']
            request.session['uphone'] = data['contact']
            request.session['username'] = username2
            request.session['password'] = password2
            request.session['uid'] = data['id']
            return redirect('userindex')
        else:
            return render(request,'login.html',{'msg':"invalid"})
    else:
        return redirect('userindex')

def logout(request):
    del request.session['username']
    del request.session['uemail']
    del request.session['uphone']
    
    del request.session['password']    
    del request.session['uid']
    return redirect('userindex')