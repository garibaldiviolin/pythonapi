from django.db import models


class Employee(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True, db_index=True)
    name = models.TextField(null=True, blank=True, unique=True)
    city = models.TextField(null=True, blank=True)
    age = models.IntegerField(null=True)
    status = models.BooleanField(null=True)
