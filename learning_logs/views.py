from django.shortcuts import render

#import models
from .models import Topic
from .models import Entry

# Create your views here.

def index(request):
    """The home page for learning_log."""
    return render(request, 'learning_logs/index.html')

def testPage(request):
    """testing a webpage for data return."""
    #get element by id where id = 'output'
    #let innerHTML of element = some data
    return render(request, 'learning_logs/testPage.html')

def topics(request):
    """web page top display all current topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics }
    return render (request, 'learning_logs/topics.html', context)