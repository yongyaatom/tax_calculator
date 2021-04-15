from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('married', views.calc, name='married'),
    path('unmarried', views.calc, name='unmarried'),
    path('calc', views.calc, name='calc'),
    path('News', views.news, name='news'),
]
