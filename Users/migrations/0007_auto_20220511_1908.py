# Generated by Django 3.2.9 on 2022-05-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0006_profile_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='About',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Country',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
