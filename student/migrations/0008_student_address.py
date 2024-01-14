from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_remove_student_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(max_length=250, null =True)
        )
    ]