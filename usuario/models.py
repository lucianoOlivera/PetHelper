from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin)
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', unique=True)
    username = models.CharField(max_length=25, unique=True)
    apellido = models.CharField(max_length=25, unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    telefono = models.CharField(max_length=20, help_text="ingrese su telefono")
    dni = models.CharField(max_length=20, help_text="ingrese su dni")
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return "@{}".format(self.username)