from django.contrib import admin

from api.models import Address, Store, Category, Product, Supplier

# Register your models here.
admin.site.register([Address, Store, Category, Product, Supplier])


"""
python manage.py makemigrations api && python manage.py migrate && python manage.py runserver
"""
