from django.db import models

# Create your models here.

class Anon(models.Model):
    post_author = models.CharField(max_length=150)
    post_name = models.CharField(max_length=100)
    post_text = models.CharField(max_length=250)
    post_date = models.CharField(max_length=100)
    post_category = models.IntegerField()
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")