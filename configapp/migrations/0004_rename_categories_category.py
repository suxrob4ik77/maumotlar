# Generated by Django 5.1.6 on 2025-03-07 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0003_news_views'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
