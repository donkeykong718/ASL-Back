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
    list_display = ('chat_box', 'user', 'message', 'timestamp')
    list_filter = ('chat_box', 'user', 'message', 'timestamp')
    search_fields = ('chat_box', 'user', 'message', 'timestamp')

class ChatBoxResource(resources.ModelResource):
    class Meta:
        model = ChatBox

class ChatBoxAdmin(ImportExportModelAdmin):
    resource_class = ChatBoxResource
    list_display = ('name', 'users')
    list_filter = ('name', 'users')
    search_fields = ('name', 'users')


admin.site.register(ChatBox, ChatBoxAdmin)
admin.site.register(Messages, MessagesAdmin)

