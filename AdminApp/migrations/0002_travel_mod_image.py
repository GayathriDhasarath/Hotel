# Generated by Django 4.2.1 on 2023-05-29 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travel_mod',
            name='image',
            field=models.ImageField(default='null.jpg', upload_to='images'),
        ),
    ]
