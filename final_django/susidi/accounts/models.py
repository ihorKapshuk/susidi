from django.db import models

# Create your models here.

class PhoneNumbers(models.Model):
    phone_number = models.CharField(max_length=10)
    is_account_created = models.BooleanField(default=False)