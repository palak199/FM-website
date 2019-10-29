from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
def signup(request):
    if request.method=='POST':
       form=UserCreationForm(request.POST) 
       if form.is_valid():
           form.save()
           return redirect('login/index.html')
       else:
           form=UserCreationForm()
           return render(request,'login/index.html',{'form':form})
           
       
def login(request):
    if request.method=='POST':
        temp='fmcrs/admin'
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            return redirect(temp)
        
        
    else:
        form=AuthenticationForm ()
        return render(request,'login/index.html',{'form':form})
       
    