# Generated by Django 4.2.7 on 2024-01-12 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_studentprofile_student'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='studentClass',
            new_name='Classs',
        ),
        migrations.RenameModel(
            old_name='studentProfile',
            new_name='Profile',
        ),
    ]
