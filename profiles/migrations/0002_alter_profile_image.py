# Generated by Django 3.2.18 on 2023-04-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_odk5vv.jpeg', upload_to='images/'),
        ),
    ]
