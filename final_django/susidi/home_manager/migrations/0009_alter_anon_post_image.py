# Generated by Django 5.0.1 on 2024-03-05 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_manager', '0008_alter_anon_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anon',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
