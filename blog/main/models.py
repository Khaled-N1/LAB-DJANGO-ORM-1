from django.db import models
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=256)
    content=models.TextField()
    publish_date =models.DateTimeField()
    category=models.CharField(max_length=10,default='none')

    