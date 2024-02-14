from django.shortcuts import render
from django.http import HttpResponse
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



def home(request):
    return render(request,'home.html')

def register(request):
    name=request.POST['name']
    password=request.POST['Password']
    address=request.POST['Address']
    mail=request.POST['Mail']
    return render(request,"output.html",{'Name':name,'Password':password,'Address':address,'Mail':mail})
    















