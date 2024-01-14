from django.db import models

# Create your models here.

class Categories(models.Model):
    class Meta:
        app_label = 'shop'

    name = models.TextField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
    

class product(models.Model):

    class Meta:
        app_label = 'shop'

    name = models.TextField(max_length=250)
    price = models.IntegerField()
    test = models.TextField(null=True, blank=True)
    categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, related_name='products')

    def __str__(self):
        return self.name

# Categories.products.all()
    # product_set