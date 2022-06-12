from django.shortcuts import render, redirect

#import models
from .models import Topic
from .models import Entry
from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """The home page for learning_log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """web page top display all current topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request,topic_id):
    """web page top display a single topic and its related entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def add_topic(request):
    """web form to add new topics"""
    if request.method != 'POST':
        # loading new empty form
        form = TopicForm()
    else:
        # Data submitted. Process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/add_topic.html', context)


def add_entry(request,topic_id):
    """add a new entry for a particular topic"""

    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # not yet posted data; load form
        form = EntryForm()
    else:
        # post request; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/add_entry.html', context)

