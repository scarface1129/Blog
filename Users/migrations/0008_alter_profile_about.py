# Generated by Django 3.2.9 on 2022-05-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20220511_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='About',
            field=models.TextField(max_length=30, null=True),
        ),
    ]