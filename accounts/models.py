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
    image = models.ImageField(upload_to='profile/', null=True)
    first_name = models.CharField(max_length=255, verbose_name="firstName")
    last_name = models.CharField(max_length=255, verbose_name="lastName")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    def __str__(self):
        return self.email



class ResetPasswordCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(unique=True, default=None, null=True, max_length=7)
    used = models.BooleanField(default=False)
