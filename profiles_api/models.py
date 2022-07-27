from django.db import models
# importing 2 classes for making custom user class
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Step5: Creating manager for our UserProfileS Model
class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("User must have an email address")
        email = self.normalize_email(email)         # Making all characters before @ case insensitive
        user = self.model(email=email, name=name)

        # NOTE: When the raw_password is None, the password will be set to an unusable password
        user.set_password(password)     # takes care of the password hashing.
        user.save(using=self._db)       # just to ensure that our application supports multiple databases
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


# Step6: Configure Django to use this UserProfiles Model as default
# AUTH_USER_MODEL = "profiles_api.UserProfiles"     add this in our settings.py file


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Step1: Create some fields for our custom user profile model
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Step2: Now Creating Model manager for this user profile class,
    # so that django knows how to create user model and how to control it.
    objects = UserProfileManager()

    # Step3: Adding some more fields to interact with admin and authentication
    USERNAME_FIELD = 'email'    # now authentication will be done via email and password, Not by username and password
    REQUIRED_FIELDS = ['name']  # Here we can insert all required fields

    # Step4: Now creating some function so that django can interact with its admin
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
