# Generated by Django 2.1.7 on 2019-05-13 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default1.jpg', upload_to='profile_pics'),
        ),
    ]
