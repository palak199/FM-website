
from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('podcast/', include('rec.urls')),
    path('events/',include('events.urls')),
    path('login/',include('login.urls'))
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
