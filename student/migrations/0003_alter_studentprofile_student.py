# Generated by Django 4.2.7 on 2024-01-12 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_studentprofile_studentclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]