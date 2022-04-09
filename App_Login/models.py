from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tenant')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Profile_setup')
    full_name = models.CharField(max_length=300, null=True)
    nid = models.IntegerField(null=True)
    phone_number = models.IntegerField(null=True)
    gender = models.CharField(max_length=30, null=True)
