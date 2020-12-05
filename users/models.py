from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(first_name=first_name,
                          last_name=last_name, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(first_name=first_name, last_name=last_name, email=email, password=password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.CharField(max_length=254, unique=True, validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9_!#$%&\'*+/=?`{|}~^-]+(?:\.[a-zA-Z0-9_!#$%&\'*+/=?`{|}~^-]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'
        )
    ])
    password = models.CharField(max_length=128, validators=[
        RegexValidator(
            regex='^[ -~]{6,}$'
        )
    ])
    first_name = models.CharField(max_length=128, validators=[
        RegexValidator(
            regex='^[a-zA-Z][a-zA-Z ,.\'-]*$'
        )
    ])
    last_name = models.CharField(max_length=128, validators=[
        RegexValidator(
            regex='^[a-zA-Z][a-zA-Z ,.\'-]*$'
        )
    ])
    is_driver = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + self.email + ')'
