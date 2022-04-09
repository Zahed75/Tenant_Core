from django.db import models
from django.contrib.auth.models import User
from App_Login.models import *


# Create your models here.
class ApartmentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flat_no = models.CharField(max_length=5000, null=True, blank=True)
    date = models.CharField(max_length=500, null=True, blank=True)


class TenantDashboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tenant_user')
    serial = models.CharField(max_length=1000, null=True, blank=True)
    types_of_bill = models.CharField(max_length=4000, blank=True, null=True)
    bill = models.CharField(max_length=3000, null=True, blank=True)
    total_amount = models.CharField(max_length=3000, null=True, blank=True)

    def __str__(self):
        return self.types_of_bill


class User_Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user')
    message = models.CharField(max_length=3000, null=True, blank=True)
    date = models.CharField(max_length=400, null=True)


class admin_dashboard(models.Model):
    user_name = models.CharField(max_length=400, null=True, blank=True)
    flat_name = models.CharField(max_length=400, null=True, blank=True)
    cost = models.CharField(max_length=400, null=True, blank=True)
    clerence = models.CharField(max_length=400, null=True, blank=True)


class Parking_Fees(models.Model):
    user = models.CharField(max_length=500, null=True, blank=True)
    cost = models.CharField(max_length=400, null=True, blank=True)
    status = models.CharField(max_length=400, null=True, blank=True)
