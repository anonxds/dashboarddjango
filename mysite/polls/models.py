from django.db import models

# Create your models here.

class Question(models.Model):
    name = models.TextField(blank=True)
    domain = models.TextField(blank=True)