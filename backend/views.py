from django.shortcuts import render,redirect,HttpResponse
from backend import models
def qwe(request):
    list=models.User.objects.all()
    return render(request,'qwe.html',{"list":list})
# Create your views here.
