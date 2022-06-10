"""Defines URL patterns for learning_logs app."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # topics page
    path('topics/', views.topics, name='topics'),
    # page for individual topics
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # page to add topic
    path('add_topic', views.add_topic, name='add_topic')
]