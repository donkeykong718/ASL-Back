# Generated by Django 4.1.7 on 2023-04-05 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_remove_conversation_all_users_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='participants',
        ),
    ]
