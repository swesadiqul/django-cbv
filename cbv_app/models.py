from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()