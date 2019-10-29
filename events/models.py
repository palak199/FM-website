from django.db import models

# Create your models here.
from django.db import models
 
class Event(models.Model):
    day = models.DateField()
    name = models.CharField(max_length=30, blank=True, null=True)

