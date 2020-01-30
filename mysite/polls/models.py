from django.db import models

# Create your models here.

class Question(models.Model):
    name = models.TextField(blank=True)
    domain = models.TextField(blank=True)


class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)