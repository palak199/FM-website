from django.db import models
class message(models.Model):
        name=models.CharField(max_length=50)
        email=models.EmailField()
        yourmessage=models.TextField()
        def __str__(self):
            return self.name
    
        


       
