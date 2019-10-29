from django.contrib import admin

# Register your models here.

from .models import Recording,Student,Team

admin.site.register(Recording)
admin.site.register(Team)
admin.site.register(Student)

