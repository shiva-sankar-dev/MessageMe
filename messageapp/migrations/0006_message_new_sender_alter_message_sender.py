# Generated by Django 5.1.4 on 2025-01-01 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0005_alter_message_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='new_sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='messageapp.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.CharField(max_length=255),
        ),
    ]
