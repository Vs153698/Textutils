from django.db import models

# Create your models here.
class Contact(models.Model):
    User_id = models.AutoField
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    text=models.TextField(max_length=600)

    def __str__(self):
        return self.name

class Contactmodal(models.Model):
    namemodal = models.CharField(max_length=30)
    emailmodal = models.EmailField()
    textmodal = models.TextField(max_length=600)

    def __str__(self):
        return self.namemodal
