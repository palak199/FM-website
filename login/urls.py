from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from django.urls import path,include
from . import views
app_name = "login"
urlpatterns = [
    path('', views.login, name='login'),
    

]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)