from django.contrib import admin

from api.models import Tag, UserProfile, Comment, Post, PostUserLikes

# each time we add a model:
admin.site.register([UserProfile, Tag, Comment, Post, PostUserLikes])

# python manage.py makemigrations api
# python manage.py migrate api
# python manage.py runserver

# visit http://localhost:8000/admin

# once per project:
# python manage.py createsuperuser
