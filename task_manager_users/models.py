import os
import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _


def user_image_file_path(instance, filename):
    """Function for creation special unique filename for image"""
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/users/", filename)


class UserManager(BaseUserManager):
    """
    Define a user manager for User model with no username field.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password"""
        if not email:
            raise ValueError("Email must be sent")
        email = self.normalize_email(email)
        # When create a user you should write password2 to check whether password was written correctly,
        # but it shouldn't be given as a parameter to user creation.
        extra_fields.pop("password2")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save regular User with the given credentials."""
        extra_fields.setdefault("is_stuff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given credentials."""
        extra_fields.setdefault("is_stuff", True)
        extra_fields.setdefault("is-superuser", True)

        if extra_fields.get("is_stuff") is not True:
            raise ValueError("Superuser must be a stuff.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Super user must be super user.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # Credentials
    username = None
    email = models.EmailField(_("email address"), unique=True)

    # User data
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    # User show for other users
    image = models.ImageField(upload_to=user_image_file_path, blank=True, null=True)
    nickname = models.TextField(blank=True, null=True, unique=True)
