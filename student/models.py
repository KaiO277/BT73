from django.db import models

# Create your models here.

class student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(max_length = 250, null= True)

    def __str__(self):
        return self.first_name
    
class Profile(models.Model):
    student = models.OneToOneField(student, on_delete=models.CASCADE)
    age = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student.first_name

class Class(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE, related_name='classSt')
    class_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.class_name    
    
# profile = Profile.objects.get(id=1)
# st = profile.profile_set.all()

# classs = Class.objects.get(id=1)
# st = student.classSt.all()

