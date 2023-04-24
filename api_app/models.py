from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    DEFAULT_DESCRIPTION = 'Без описания'

    avatar = models.ImageField(upload_to='avatars/')
    description = models.TextField(default=DEFAULT_DESCRIPTION)

    scores = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)


class Theme(models.Model):
    name = models.TextField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='question_author')

    best_answer = models.ForeignKey('Answer', blank=True, null=True, on_delete=models.CASCADE, related_name='best_answer')

    themes = models.ManyToManyField('Theme', related_name='question_themes')

    title = models.TextField()
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
