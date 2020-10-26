from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, PermissionsMixin


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse("person_list")


class NewUser(User, PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)


class CustomerEntry(models.Model):
    rst_number = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    vehicle_number = models.CharField(max_length=10)
    charges = models.IntegerField()
    tare_weight = models.IntegerField()
    gross_weight = models.IntegerField(null=True, blank=True)
    net_weight = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.customer_name

