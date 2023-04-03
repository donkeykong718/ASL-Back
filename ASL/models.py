from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField




# Create your models here.

class ChatBox(models.Model):
    name = models.CharField(max_length=100)
    users = ArrayField(models.CharField(max_length=100), blank=True, null=True, default=list)
    all_messages = ArrayField(models.CharField(max_length=1000), blank=True, null=True, default=list)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'chat_box'
  
  
  
class Messages(models.Model):
    chat_name = models.ForeignKey(ChatBox, related_name='%(class)s_room', on_delete=models.CASCADE, default='')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.message
  
    class Meta:
      db_table = 'messages'
  