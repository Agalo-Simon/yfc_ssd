from tabnanny import verbose
from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='staff/', blank=True, null=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name ='Staff Team'

    def __str__(self):
        return self.name

    

