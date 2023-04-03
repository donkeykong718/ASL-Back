# Generated by Django 4.2 on 2023-04-03 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ASL', '0002_rename_user_messages_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbox',
            name='creator',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='chat_box', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]