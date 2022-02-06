"""Defines URL patterns for learning_logs app."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #duplicate home page
    path('2', views.index, name = 'index'),
    #test page
    path('test/', views.testPage, name = 'test page'),
    #topics page
    path('topics/', views.topics, name = 'topics')
]