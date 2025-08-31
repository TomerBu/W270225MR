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
    name = models.CharField(max_length = 100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.address.city}, {self.address.street}"