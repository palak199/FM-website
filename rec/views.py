from django.shortcuts import render, get_object_or_404,redirect
from .models import Recording,Student,Team,message
from .forms import messageform
# Create your views here.
def podcast(request):
    template='rec/podcast.html'
    recording = Recording.objects.all()
    context={
    
        'recording':recording
        
    }
    return render(request,template,context)





           
       

       