# Generated by Django 4.2.7 on 2024-01-14 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='test',
        ),
    ]
