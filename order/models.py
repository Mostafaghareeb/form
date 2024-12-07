from django.db import models

# Create your models here.
class Form(models.Model):
    name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=4, decimal_places=0)
    message = models.TextField(max_length=200)
    def __str__(self):
        return (self.name)
    class Meta:
        verbose_name = 'message'    
    
