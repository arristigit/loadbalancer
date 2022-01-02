from django.db import models

class SmsProvider(models.Model):
    text = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f'{self.phone} - {self.text}'