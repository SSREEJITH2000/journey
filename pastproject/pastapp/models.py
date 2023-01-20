from django.db import models

# Create your models here.
class venue(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pics')
    des = models.TextField()

    def __str__(self):
        return self.name

class doc(models.Model):
    img=models.ImageField(upload_to='docs')
class team(models.Model):
    image=models.ImageField(upload_to='tesa')
    names=models.CharField(max_length=300)
    description=models.TextField()

    def __str__(self):
        return self.names






