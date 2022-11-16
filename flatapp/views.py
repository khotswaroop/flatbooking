from django.http import HttpResponse
from django.shortcuts import redirect, render
from flatapp.models import Registration,FlatBooking
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from flatapp.forms import RegisterForm
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        add=request.POST['add']
        uname=request.POST['uname']
        passrd=request.POST['passrd']
        detid=request.POST['detid']
        # print(fname,lname,address,uname,upass,cpass)
        regt=Registration.objects.create(firstName=fname,lastName=lname,address=add,username=uname,password=passrd,date=detid)
        regt.save()
        return redirect('/register')
    else:
        return render(request,'register.html')

def bookflat(request):
    if request.method=='POST':
        city=request.POST['city']
        residencyname=request.POST['residencyname']
        flatno=request.POST['flatno']
        flowrno=request.POST['flowrno']
        date=request.POST['date']
        residencyname=request.POST['residencyname']
        # print(city,residencyname)
        book=FlatBooking.objects.create(City=city,ResidencyName=residencyname,FlatNomber=flatno,FlowrNomber=flowrno,Date=date)
        book.save()
        return render(request,'bookflat.html')
    else:
        return render(request,'bookflat.html')

def showflats(request):
    booking=FlatBooking.objects.all()
    return render(request,'showbooking.html',{'data':booking})

def mumbai(request):
    mumbai=FlatBooking.objects.filter(City='mumbai')
    return render(request,'showbooking.html',{'data':mumbai})

def bangalore(request):
    bangalore=FlatBooking.objects.filter(City='Bangalore')
    return render(request,'showbooking.html',{'data':bangalore})

def pune(request):
    pune=FlatBooking.objects.filter(City='Pune')
    return render(request,'showbooking.html',{'data':pune})

def delhi(request):
    delhi=FlatBooking.objects.filter(City='delhi')
    return render(request,'showbooking.html',{'data':delhi})

def residency(request):
    residency=FlatBooking.objects.filter(ResidencyName='Plaza')
    return render(request,'showbooking.html',{'data':residency})

def deleteflats(request,rid):
    remove_flat=FlatBooking.objects.filter(id=rid)
    remove_flat.delete()
    return redirect('/showbooking')

def updateflats(request,rid):
    if request.method=='POST':
        city=request.POST['city']
        residencyname=request.POST['residencyname']
        flatno=request.POST['flatno']
        flowrno=request.POST['flowrno']
        date=request.POST['date']
        residencyname=request.POST['residencyname']
        update_flat=FlatBooking.objects.filter(id=rid)
        update_flat.update(City=city,ResidencyName=residencyname,FlatNomber=flatno,FlowrNomber=flowrno,Date=date)
        return render(request,'bookflat.html')
    else:
        data=FlatBooking.objects.filter(id=rid)
        return render(request,'updateflat.html',{'data':data})

# def registration(request):
#     if request.method=='POST':
#         uname=request.POST['username']
#         pass1=request.POST['password1']
#         # print(uname,pass1)
#         # u1=User(username=uname,password=pass1,is_staff=True,is_active=True)
#         # u1.save()
#         return redirect('/registration')
#     else:
#         form=UserCreationForm()
#         return render(request,'signup.html',{'form':form})

# def registration(request):
#     if request.method=='POST':
#         fm=UserCreationForm(request.POST)
#         # print(fm)
#         print(fm.is_valid())
#         if fm.is_valid():
#             fm.save()
#         return redirect('/registration')
#     else:
#         fm=UserCreationForm(request.POST)
#         return render(request,'signup.html',{'form':fm})


def registration(request):
    if request.method=='POST':
        fm=RegisterForm(request.POST)
        # print(fm)
        # print(fm.is_valid()) 
        if fm.is_valid():
            fm.save()
        return redirect('/registration')
    else:
        fm=RegisterForm(request.POST)
        return render(request,'signup.html',{'form':fm})

def login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        # print(fm)
        # print(fm.is_valid())
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            u=authenticate(username=uname,password=upass)
            print(u)
            if u:
                return redirect('/')
    else:
        fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})  