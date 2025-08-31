from django.db import models


class Address(models.Model):
    # fields:
    street = models.CharField(max_length=100)
    apartment = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default='IL')

    # str method
    def __str__(self):
        return f"{self.street}, {self.city}, {self.apartment} {self.zip_code}, {self.country}"


class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.address.city}, {self.address.street}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    # Foreign key = OneToMany
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    stores = models.ManyToManyField(Store)

    def __str__(self):
        return self.name