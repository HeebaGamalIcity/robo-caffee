from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):
    USER_TYPE_CHOICES = [
        (1, 'admin'),
        (2, 'technetium'),
        (3, 'operator'),
    ]

    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email



class ResetPasswordCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(unique=True, default=None, null=True, max_length=7)
    used = models.BooleanField(default=False)
