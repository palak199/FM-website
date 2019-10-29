from django.shortcuts import render,get_object_or_404,redirect
from .models import message
from .forms import messageform
def index(request):
    template='fmcrs/index.html'
    return render(request,template)
def about(request):
    template='fmcrs/about.html'
    return render(request,template)
def contact(request):
    template='fmcrs/contact.html'
    form=messageform(request.POST) 
    if form.is_valid():
           form.save()
           return redirect('contact')
    else:
           form=messageform()
           return render(request,template,{'form':form})

