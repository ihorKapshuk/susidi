# Generated by Django 5.0.1 on 2024-03-05 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_manager', '0005_remove_anon_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anon',
            name='post_author',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='anon',
            name='post_text',
            field=models.CharField(max_length=250),
        ),
    ]
