from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = HTMLField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
