# Generated by Django 5.1.4 on 2025-01-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0008_rename_new_sender_message_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='profile_image/profile.png', null=True, upload_to='profile_image'),
        ),
    ]
