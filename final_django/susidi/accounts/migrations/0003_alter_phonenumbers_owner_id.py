# Generated by Django 5.0.1 on 2024-03-04 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_phonenumbers_owner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumbers',
            name='owner_id',
            field=models.CharField(max_length=30),
        ),
    ]
