from django.shortcuts import render, redirect



def home(request):
    return render(request,'home.html', {'name':'Elyor'})

def addPage(request):
    return render(request, 'addform.html')

def add(request):
    # print(request.POST)
    # print(request.POST.get('num1')) 
    # print(request.POST.get('num2')) 

    val1 = int(request.POST.get('num1'))
    val2 = int(request.POST.get('num2'))

    result = val1 + val2

    return render(request, 'result.html', {'result':result})






