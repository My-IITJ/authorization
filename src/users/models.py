from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.management.utils import get_random_secret_key

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

    email = models.EmailField(unique=True, db_index=True)
    secret_key = models.CharField(max_length=255, default=get_random_secret_key)
    jwt_token = models.CharField(max_length=1000, null=True, blank=True)

    REQUIRED_FIELDS = ['email']

    class Meta:
        swappable = 'AUTH_USER_MODEL'

    @property
    def name(self):
        if not self.last_name:
            return self.first_name.capitalize()

        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'


class UserRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=25, choices=EVENT_CHOICES, default='Student')
    verification_status = models.CharField(max_length=100, null=True, blank=True)
