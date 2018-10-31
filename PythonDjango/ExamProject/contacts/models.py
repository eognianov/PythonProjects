from django.db import models
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    work_phone = models.IntegerField(null=True, blank=True)
    mobile_phone = models.IntegerField(null=True, blank=True)

    is_private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    author = models.ForeignKey('accounts.UserAccount', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name

