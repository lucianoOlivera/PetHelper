from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
    Group)
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

dni_regex = RegexValidator(regex=r"^[\d]{1,3}\.?[\d]{3,3}\.?[\d]{3,3}$", message="El formato de DNI debe tener 8 caracteres numericos")


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
    permiso = models.ForeignKey(Group, null=True, on_delete=models.CASCADE, default=1)
    apellido = models.CharField(max_length=25)
    date_joined = models.DateTimeField(default=timezone.now)
    DNI = models.CharField(max_length=8, default="", validators=[dni_regex])
    foto = models.ImageField(upload_to="usuario",blank=True, null=True)
    telefono = models.CharField(max_length=10, null=True, default="", help_text="Ejemplo: 2614247398")
    objects = UserManager()
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return "@{}".format(self.username)
