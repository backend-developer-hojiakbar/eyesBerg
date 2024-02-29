from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    ROLE_CHOICES = (
        ('cleaner', 'Cleaner'),
        ('waiter', 'Waiter'),
        ('admin', 'Admin'),
        ('sub_admin', 'Sub-Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='waiter')

    def __str__(self):
        return self.user.username

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
