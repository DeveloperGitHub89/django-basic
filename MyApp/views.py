from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def openIndexPage(request):
    cityNames=['Gwalior','Mumbai',"Delhi",'Indore']
    return render(request, 'index.html',{'name':'Rohan','age':23,'cities':cityNames})

def openForm(request):
    return render(request,'form.html')

def sum(request):
    # a=int(request.GET['n1'])
    # b=int(request.GET['n2'])
    a=int(request.POST['n1'])
    b=int(request.POST['n2'])
    c=a+b
    return render(request,'form.html',{'sum':c})

def product(request):
    a=9
    b=3
    c=a*b
    return HttpResponse(c)
