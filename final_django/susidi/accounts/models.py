from django.db import models

# Create your models here.

class PhoneNumbers(models.Model):
    owner_id = models.IntegerField(default=None)
    phone_number = models.CharField(max_length=10)
    is_account_created = models.BooleanField(default=False)