from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/brand', null=True, blank=True)

    @staticmethod
    def get_all_brand():
        return Brand.objects.all()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 200)

    @staticmethod
    def get_all_category():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField(default = 0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length = 200, default = '')
    image = models.ImageField(upload_to='media/product/')

    @staticmethod
    def get_all_product():
        return Product.objects.all()
    
    def __str__(self):
        return self.name