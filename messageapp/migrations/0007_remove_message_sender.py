# Generated by Django 5.1.4 on 2025-01-01 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0006_message_new_sender_alter_message_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='sender',
        ),
    ]
