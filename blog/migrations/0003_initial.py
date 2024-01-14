# Generated by Django 4.2.7 on 2024-01-13 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('test', models.CharField(blank=True, null=True)),
            ],
        ),
    ]