from django.db import models

# Create your models here.
class Champion(models.Model):
    number = models.IntegerField(null=True,blank=True,)
    image = models.ImageField(null=True,blank=True)
    name = models.CharField(null=True,blank=True,max_length=200)
    
    def __str__(self):
        return self.name