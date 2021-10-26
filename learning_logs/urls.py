"""Определяет схемы URL для learning_logs."""

from . import views
from django.urls import path

import learning_logs


urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
    #page with Topic
    path('topics/', views.topics, name='topics'),
    #page with topic description
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    #page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #page for edit entries
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
]
