from django.db import models
from django.contrib.auth.models import AbstractUser

EVENT_CHOICES = (
    ('guest', 'Guest'),
    ('faculty', 'Faculty'),
    ('staff', 'Staff'),
    ('student', 'Student'),
    ('alumni', 'Alumni'),
)

class CustomUser(AbstractUser):
    last_logout = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

class UserRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=25, choices=EVENT_CHOICES, default='Student')
    verification_status = models.CharField(max_length=100, null=True, blank=True)
