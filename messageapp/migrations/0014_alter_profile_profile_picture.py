# Generated by Django 5.1.4 on 2025-01-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0013_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profile_image/profile.png', null=True, upload_to='profile_image'),
        ),
    ]
