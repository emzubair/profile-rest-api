from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """docstring for UserProfileManager."""

    def create_user(self,email,name,password=None):
        """Creates a new user Profile."""
        if not email:
            raise ValueError("User must have an email address.")
        email = self.normalize_email(email)
        user = self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_super_user(self,email,name,password):
        """Creates and store a new Superuser with given Details."""
        user = self.create_user(email,name,password)
        user.is_super_user = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """represents a "user profile" inside the system"""
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=225)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get user's Full Name."""
        return self.name

    def get_short_name(self):
        """used to get user's Short Name"""
        return self.name

    def ___str___(self):
        """Django uses it when it needs to convert the object to Strings"""
        return self.email
