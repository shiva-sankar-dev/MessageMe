# Generated by Django 5.1.4 on 2025-01-01 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0003_alter_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(max_length=255),
        ),
    ]