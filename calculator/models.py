from django.db import models

# Create your models here.


class News(models.Model):
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    reporter = models.CharField(max_length=40)
    news_header = models.CharField(max_length=200)
    news = models.TextField()
