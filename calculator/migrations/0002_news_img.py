# Generated by Django 2.2.12 on 2021-05-12 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
