from django.db import models

class Address(models.Model):
    street = models.CharField(max_length=100)
    apartment = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=50)
    
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50, default='IL')

    def __str__(self):
        return f"{self.street}, {self.city}, {self.apartment} {self.zip_code}, {self.country}"