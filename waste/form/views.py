from django.shortcuts import render
from .forms import userform
# Create your views here.

def index(request):
    form=userform
    content={'form':form,}
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'index.html',content)
