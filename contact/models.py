from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Contact(models.Model):

    contact_title = models.CharField(max_length=200)
    contact_body = models.TextField(blank=True)
    email = models.CharField(max_length=200)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.contact_title
        