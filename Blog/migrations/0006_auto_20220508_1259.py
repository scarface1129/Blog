# Generated by Django 3.2.9 on 2022-05-08 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Blog.blogcategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogs',
            name='media',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='precont',
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
    ]