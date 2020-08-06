from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Comment(models.Model):

    comment_body = models.TextField()
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_body
