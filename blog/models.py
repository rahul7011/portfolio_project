from django.db import models

# Create your models here.

class blog(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=225)