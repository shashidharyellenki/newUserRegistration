from django.shortcuts import redirect, render
from . models import Register
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def index(request):
    if request.method=='POST':
        FirstName = request.POST['FirstName']
        LastName = request.POST['LastName']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        password2 = request.POST['password2']
        Birthday_date = request.POST['Birthday_date']
        username = request.POST['Username']
        if password == password2:
            if Register.objects.filter(email=email).exists():
                return HttpResponse("emial already in use")
            else:
                register = Register(FirstName= FirstName,LastName=LastName,email=email, phone=phone, password=password, password2=password2,Birthday_date=Birthday_date, username=username)
                register.save()
                context={
                    "firstname":FirstName,
                    "Lastname":LastName
                }
                return render(request, 'pagess/register.html', context)
        else:
            return HttpResponse("password do not match")
    else:

        return render(request, 'pagess/index.html')


def login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']

        if Register.objects.filter(username=Username).exists():
            if Register.objects.filter(password=password).exists():
                context={
                    "username":Username
                }
                return render(request, 'pagess/login.html',context)
            else:
                return HttpResponse("Wrong password")
        else:
            return HttpResponse("Invalid username")
    else:
        return render(request,'pagess/index.html')

