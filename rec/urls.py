
from django.urls import path
from . import views

app_name='rec'
urlpatterns = [
    
    path('', views.podcast, name='podcast'),
    
]

