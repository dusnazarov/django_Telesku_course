from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



def home(request):
    return render(request,'home.html', {'title':'Home Page'})

def addPage(request):
    return render(request, 'addform.html')

def add(request):
    # print(request.POST)
    # print(request.POST.get('num1')) 
    # print(request.POST.get('num2')) 

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
                print('Username Taken')
            elif User.objects.filter(email=email).exists():
                print('Email Taken')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                user.save()
                print('User Created')
        else:
            print('Password Not Matching...')            
        return redirect('home')

    
    else:    
        
        return render(request,'register.html')




    




    





