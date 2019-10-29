from django.forms import ModelForm
from .models import message

class messageform(ModelForm):
    
    class Meta:
        model = message
        fields = ("name","email", "yourmessage",)

       