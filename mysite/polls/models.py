from django.db import models

# Create your models here.


class all_breaches(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    domain = models.CharField(max_length=100, blank=True)
    time_breached = models.IntegerField(blank=True, null=True)

class infected_email(models.Model):
    email = models.TextField(blank=True)
    site = models.TextField(blank=True)


class list_email(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(blank=True)