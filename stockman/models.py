from django.db import models


class Categories(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Products(models.Model):
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name + "," + str(self.price)
