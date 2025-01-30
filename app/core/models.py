"""
<<<<<<< HEAD
database models
"""
=======
Database models.
"""
from django.conf import settings
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

class UserManager(BaseUserManager):
<<<<<<< HEAD
    # manager for u1

    def create_user(self, email, password=None, **extra_fields):
        # create save and return a new user
        if not email:
            raise ValueError('User must have an email address')
=======
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
<<<<<<< HEAD
        #create and return a new superuser
=======
        """Create and return a new superuser."""
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

<<<<<<< HEAD
class User(AbstractBaseUser, PermissionsMixin):
    # user in the system
=======

class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

<<<<<<< HEAD
    objects=UserManager()

    USERNAME_FIELD = 'email'
=======
    objects = UserManager()

    USERNAME_FIELD = 'email'

class Recipe(models.Model):
    # recipe object
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title
>>>>>>> 11a424c09313af2d3ebfccd2f858b976cb12a05b
