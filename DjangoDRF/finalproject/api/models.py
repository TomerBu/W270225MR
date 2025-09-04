from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # computed property:
    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return f'Profile of {self.user.username}'

    def __repr__(self):
        return f'UserProfile(user={self.user.username}, bio={self.bio}, birth_date={self.birth_date})'


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=32)

    def __str__(self):
        return f'{self.name}'


STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived'),
)


class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, validators=[
        MinLengthValidator(5),
        RegexValidator(r'^[\w\s]+$', 'Title must be alphanumeric.')
    ])
    text = models.TextField(validators=[MinLengthValidator(5)])
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Post: {self.title} by {self.author.user.username}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField(validators=[MinLengthValidator(5)], max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    reply_to = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author.user.username} on {self.post.title}'


LIKE_CHOICES = (
    ('like', 'Like'),
    ('dislike', 'Dislike'),
)


class PostUserLikes(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_type = models.CharField(choices=LIKE_CHOICES, default="like")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # a user can't like a post twice
    class Meta:
        unique_together = ['user', 'post']

    def __str__(self):
        return f"{self.user.username} {self.like_type}d {self.post.title}"
