from django.shortcuts import render

#import models
from .models import Topic
from .models import Entry

# Create your views here.

def index(request):
    """The home page for learning_log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """web page top display all current topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics }
    return render (request, 'learning_logs/topics.html', context)

def topic(request,topic_id):
    """web page top display a single topic and its related entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries' : entries }
    return render (request, 'learning_logs/topic.html', context)
