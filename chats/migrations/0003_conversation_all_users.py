# Generated by Django 4.1.7 on 2023-04-05 02:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats', '0002_remove_message_to_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='all_users',
            field=models.ManyToManyField(related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]
