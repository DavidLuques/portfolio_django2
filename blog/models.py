from django.db import models
import datetime

# Create your models here.
class project(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=250)
    image=models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)

class Post(models.Model):
    title=models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    date=models.DateField(datetime.date.today)


