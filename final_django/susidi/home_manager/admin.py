from django.contrib import admin
from accounts.models import PhoneNumbers
from .models import Anon, Comment

# Register your models here.

admin.site.register(PhoneNumbers)
admin.site.register(Anon)
admin.site.register(Comment)