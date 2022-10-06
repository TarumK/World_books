from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=40)

class Subscriber(models.Model):

    name = models.CharField(max_length=128)
    email = models.EmailField

    def __str__(self):
        return "User %s" % (self.name)
