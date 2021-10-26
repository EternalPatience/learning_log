from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING

class Topic(models.Model):
    """Theme which is investigated by user"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Returns a string with model description"""
        return self.text
    
class Entry(models.Model):
    """Information about Topic"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text   
        
