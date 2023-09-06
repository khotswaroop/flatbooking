from django.http import HttpResponse
from django.shortcuts import redirect, render
from flatapp.models import Registration,FlatBooking,AddContact,AddContactUs
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from flatapp.forms import RegisterForm
from django.contrib.auth import authenticate

# Create your views here.

def index(request):
    return render(request,'index.html')

def addcontact(request):
    if request.method=='POST':
        City=request.POST['city']
        Address=request.POST['address']
        Phone=request.POST['phone']
        Email=request.POST['email']
        data=AddContact.objects.create(city=City,address=Address,phone=Phone,email=Email)
        data.save()
        return redirect('/contact')
    else:
        return render(request,'addcontact.html')

def showcontact(request):
    data=AddContact.objects.all()
    return render(request,'showcontact.html',{'data':data})

def addcontactus(request):
    if request.method=='POST':
        Name=request.POST['name']
        ContactUs=request.POST['contactus']
        Email=request.POST['email']
        data=AddContactUs.objects.create(name=Name,contactus=ContactUs,email=Email)
        data.save()
        return render(request,'footer.html')
    else:
        return render(request,'footer.html')

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
        return render(request,'register.html')
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
        book=FlatBooking.objects.create(City=city,ResidencyName=residencyname,FlatNomber=flatno,FlowrNomber=flowrno,Date=date)
        book.save()
        msg='Data Save Successfully'
        return render(request,'bookflat.html',{'msg':msg})
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
        return redirect('/edit')
    else:
        data=FlatBooking.objects.filter(id=rid)
        return render(request,'editflat.html',{'data':data})


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

def about(request):
    return render(request,'about.html')

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
            return HttpResponse('<h2>Enter Correct Username And Password</h2>')
    else:
        fm=AuthenticationForm()
        return render(request,'login.html',{'form':fm})  