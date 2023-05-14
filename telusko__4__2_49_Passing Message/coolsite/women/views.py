from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages



def home(request):
    return render(request,'home.html', {'title':'Home Page'})

def addPage(request):
    return render(request, 'addform.html')

def add(request):
    
    val1 = int(request.GET.get('num1'))
    val2 = int(request.GET.get('num2'))

    result = val1 + val2

    return render(request, 'result.html', {'result':result})


def register(request):
    if request.method == 'POST':        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
               messages.info(request, 'Email Taken')
               return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                messages.info(request, 'User Created')
                return redirect('register')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')            
            
    else:    
        
        return render(request,'register.html')




    




    





