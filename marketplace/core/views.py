from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    products=Product.objects.all()
    return render(request,'index.html',{'products':products})


def detail(request,id):
    products=Product.objects.get(id=id)
    return render(request,'detail.html',{'product':products})
