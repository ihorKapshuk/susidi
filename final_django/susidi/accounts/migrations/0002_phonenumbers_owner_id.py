# Generated by Django 5.0.1 on 2024-03-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phonenumbers',
            name='owner_id',
            field=models.IntegerField(default=None),
        ),
    ]
