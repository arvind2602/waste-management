from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from form import forms

def index(request):
    if request.method=="POST":
        username=request.POST['name']
        phone=request.POST['phone']
        donation=request.POST['donation']
        address=request.POST['address']
        message=request.POST['text']
        user=User.objects.create_user(username,phone,donation,address,message)
        user.save()
        return redirect(request,'/')
    return render(request,'index.html')
def forms(request):
    return render(request,)