from django.shortcuts import render,redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from userapp.models import *

# Create your views here.
def AddHotel(request):
    return render(request,'AddHotel.html')
def ViewHotel(request):
    data=Viewtable.objects.all()

    return render(request,'ViewHotel.html',{'data':data}) 

def hotel(request):
    if (request.method=='POST'):
        hotel_name=request.POST['hotel_name']
        hotel_description=request.POST['hotel_description']
        booking_price=request.POST['booking_price']
        image=request.FILES['image']
        data=Viewtable(name=hotel_name,desc=hotel_description,price=booking_price,image=image)
        data.save()
        return redirect('ViewHotel')
def edit(request,id):
    data=Viewtable.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})

def update(request,id):
    if (request.method=='POST'):
        hotel_name=request.POST['hotel_name']
        hotel_description=request.POST['hotel_description']
        booking_price=request.POST['booking_price']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Viewtable.objects.get(id=id).image
        Viewtable.objects.filter(id=id).update(name=hotel_name,desc=hotel_description,price=booking_price,image=file)
        return redirect('ViewHotel')
def delete(request,id):
    Viewtable.objects.filter(id=id).delete()
    return redirect('ViewHotel')
def adminindex(request):
    return render(request,'adminindex.html')
def sample(request):
    return render(request,'sample.html')
def demo(request):
    return render(request,'demo.html')
def travel(request):
    return render(request,'travel.html')
def travel_table(request):
    data=Travel_mod.objects.all()
    return render(request,'travel_table.html',{'data':data})
def datas(request):
    if(request.method=='POST'):
        dest=request.POST['dest']
        desc=request.POST['desc']
        price=request.POST['price']
        image=request.FILES['image']
        data=Travel_mod(dest=dest,desc=desc,price=price,image=image)
        data.save()
        return redirect('travel_table')

def travel_edit(request,id):
    data=Travel_mod.objects.filter(id=id)
    return render(request,'travel_edit.html',{'data':data})
def travel_update(request,id):
     if(request.method=='POST'):
        dest=request.POST['dest']
        desc=request.POST['desc']
        price=request.POST['price']
        try:
            img_c=request.FILES['image']
            fs=FileSystemStorage()
            file=fs.save(img_c.name,img_c)
        except MultiValueDictKeyError:
            file=Travel_mod.objects.get(id=id).image
        Travel_mod.objects.filter(id=id).update(dest=dest,desc=desc,price=price,image=file)
        return redirect('travel_table')
def travel_delete(request,id):
    Travel_mod.objects.filter(id=id).delete()
    return redirect('travel_table')
def user_message(request):
    data=Contact_details.objects.all()
    return render(request,'user_message.html',{'data':data})
def userdetails_delete(request,id):
    Contact_details.objects.filter(id=id).delete()
    return redirect('user_message')