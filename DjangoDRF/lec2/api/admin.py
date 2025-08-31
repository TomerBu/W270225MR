from django.contrib import admin

from api.models import Address, Store, Category, Product

# Register your models here.
admin.site.register([Address, Store, Category, Product])


"""
python manage.py makemigrations api
python manage.py migrate
python manage.py runserver
"""
