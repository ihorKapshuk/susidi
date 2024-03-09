from django.contrib import admin
from .models import Anon, Comment

# Register your models here.

admin.site.register(Anon)
admin.site.register(Comment)