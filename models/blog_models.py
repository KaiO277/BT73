from django.db import models

# Create your models here.

class post(models.Model):

    class Meta:
        app_label = 'blog'

    title = models.TextField(max_length=250)
    description = models.TextField(max_length = 250)
    # test = models.CharField(null=True, blank=True)

    def __str__(self):
        return self.title