from django.contrib import admin
from .models import ChatBox, Messages
from import_export import resources
from import_export.admin import ImportExportModelAdmin



# Register your models here.

class MessagesResource(resources.ModelResource):
    class Meta:
        model = Messages

class MessagesAdmin(ImportExportModelAdmin):
    resource_class = MessagesResource
    list_display = ('chat_name', 'user', 'message', 'timestamp')
    list_filter = ('chat_name', 'user', 'message', 'timestamp')
    search_fields = ('chat_name', 'user', 'message', 'timestamp')

class ChatBoxResource(resources.ModelResource):
    class Meta:
        model = ChatBox

class ChatBoxAdmin(ImportExportModelAdmin):
    resource_class = ChatBoxResource
    list_display = ('name', 'users', 'all_messages')
    list_filter = ('name', 'users', 'all_messages')
    search_fields = ('name', 'users', 'all_messages')

admin.site.register(ChatBox, ChatBoxAdmin)
admin.site.register(Messages, MessagesAdmin)

