from django.contrib import admin
from accounts.models import PhoneNumbers
from .models import Anon

# Register your models here.

admin.site.register(PhoneNumbers)
admin.site.register(Anon)