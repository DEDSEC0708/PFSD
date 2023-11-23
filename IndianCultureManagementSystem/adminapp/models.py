from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class Admin(models.Model):
    username = models.CharField(max_length=100, default=False)
    Email = models.CharField(max_length=100, blank=False)
    Password = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.Email


class User(models.Model):
    Full_Name = models.CharField(max_length=100, blank=False, unique=True)
    E_mail = models.CharField(max_length=100, blank=False)
    Gender_choices = (("Male", "Male"), ("Female", "Female"), ("Other", "Other"))
    Gender = models.CharField(max_length=20, blank=False, choices=Gender_choices)
    password = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table = "user_table"

    def __str__(self):
        return self.Full_Name


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password, full_name, gender, **extra_fields):
        if not username:
            raise ValueError('Users must have a username')

        if not email:
            raise ValueError('Users must have an email address')

        if not full_name:
            raise ValueError('Users must have a full name')

        if not gender:
            raise ValueError('Users must have a gender')

        user = self.model(username=username, email=self.normalize_email(email), full_name=full_name, gender=gender,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
