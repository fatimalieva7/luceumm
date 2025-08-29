from django.urls import path
from . import views






urlpatterns = [
path('about', views.about, name='about'),
path('team', views.team, name='team'),
path('courses', views.courses, name='courses'),
    path('profession', views.profession, name='profession'),

    ]