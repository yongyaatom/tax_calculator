# Generated by Django 2.2.12 on 2021-05-12 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_news_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
