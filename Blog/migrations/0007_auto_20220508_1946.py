# Generated by Django 3.2.9 on 2022-05-08 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_auto_20220508_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
