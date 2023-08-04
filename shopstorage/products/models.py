from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count_on_stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.price} - {self.category}'

class Client(models.Model):
    name = models.CharField(max_length=70)
    order = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.name} - {self.order}'