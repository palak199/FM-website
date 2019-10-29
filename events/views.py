from django.shortcuts import render,get_object_or_404
from .models import Event
# Create your views here.
def calender(request):
    event=Event.objects.all()
    context={
        'event':event
    }
    template='events/calender.html'
    return render(request, template, context)