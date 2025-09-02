from django.contrib import admin

from api.models import Student, Kitten

# Register your models here.

admin.site.register([Student, Kitten])

"""
python manage.py createsuperuser 
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver

python manage.py makemigrations && python manage.py migrate && python manage.py runserver
"""