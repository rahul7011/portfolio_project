from django.db import models

# Create your models here.

class blog(models.Model):
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=225)

    def summary(self):
        return self.body[:150]

    def cropdate(self):
        return self.pub_date.strftime('%b %e %Y ')

    def __str__(self):
        return self.title