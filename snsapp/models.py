from django.db import models

# Create your models here.

class SnsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimage = models.ImageField(upload_to='')
    good = models.IntegerField(default=0, blank=True, null=True)
    read = models.IntegerField(default=0, blank=True, null=True)
    readtext = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title