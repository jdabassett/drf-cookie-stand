from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    # forces email to be unique
    email = models.EmailField(_("Email Address"), unique=True)

    def __str__(self):
        return self.username
