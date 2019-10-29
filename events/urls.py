
from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='events'
urlpatterns = [

    path('', views.calender, name='calender'),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
