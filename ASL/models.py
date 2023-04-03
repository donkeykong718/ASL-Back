from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField




# Create your models here.

class ChatBox(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='chat_box')
    messages = ArrayField(models.CharField(max_length=1000), blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'chat_box'
  
  
  
class Messages(models.Model):
    chat_box = models.ForeignKey(ChatBox, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
  
    class Meta:
      db_table = 'messages'
  