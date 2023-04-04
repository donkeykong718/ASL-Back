from django.contrib import admin
from .models import Conversation, Message
from import_export import resources
from import_export.admin import ImportExportModelAdmin



# Register your models here.
admin.site.register(Conversation)
admin.site.register(Message)