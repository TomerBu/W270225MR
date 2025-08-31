from django.contrib import admin

from api.models import Address

# Register your models here.
admin.site.register([Address])


"""
python manage.py makemigrations api
python manage.py migrate
python manage.py runserver
"""
