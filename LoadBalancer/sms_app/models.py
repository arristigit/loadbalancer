from os import name
from django.db import models

class Sms(models.Model):
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='Data/')

    def __str__(self):
        return f'{self.name}'