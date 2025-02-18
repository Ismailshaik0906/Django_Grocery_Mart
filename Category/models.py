from django.db import models

# Create your models here.
class Category(models.Model):
    cat_id=models.CharField(max_length=15,primary_key=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    images=models.ImageField(upload_to='category')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    images=models.ImageField(upload_to='product')

    def __str__(self):
        return self.name
    

