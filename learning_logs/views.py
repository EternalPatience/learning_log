from django import http
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, request
from django.urls import conf

import learning_logs
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """Homepage if app Learning log"""
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """List of topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    """return 1 topic and all  its entries"""
    topic = get_object_or_404(id=topic_id)

    # check owner
    check_topic_owner(request, topic)

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def check_topic_owner(request, topic):
    topic = topic
    request = request
    if topic.owner != request.user:
        raise Http404




@login_required
def new_topic(request):
    """New theme"""
    if request.method != 'POST':
        # Data was not got, create an empty form
        form = TopicForm()
    else:
        # Post data was sent, save it
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('topics')

    # Return an empty form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for certain topic"""
    topic = get_object_or_404(id=topic_id)
    check_topic_owner(request, topic)
    if request.method != 'POST':
        # Data was not got, create an empty form
        form = EntryForm()
    else:
        # Post data was sent, save it
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topic', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit current entry"""
    entry = get_object_or_404(id=entry_id)
    topic = entry.topic
    # check owner
    check_topic_owner(request, topic)

    if request.method != "POST":
        # Исходный запрос, форма заполняется данными текущей записи
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST, обработать данные
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
