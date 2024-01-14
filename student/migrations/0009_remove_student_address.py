from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_student_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='address',
        )
    ]