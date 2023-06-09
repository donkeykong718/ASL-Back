# Generated by Django 4.1.7 on 2023-04-05 02:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0003_conversation_all_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='all_users',
        ),
        migrations.AddField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(related_name='messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
