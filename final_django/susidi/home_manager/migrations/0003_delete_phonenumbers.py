# Generated by Django 5.0.1 on 2024-02-27 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_manager', '0002_rename_pnonenumbers_phonenumbers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhoneNumbers',
        ),
    ]
