from django import forms
from .models import message

class messageform(forms.ModelForm):
    class Meta:
        model = message
        fields = ("name","email", "yourmessage",)

