from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MyUserManager

class User(AbstractBaseUser):
    email = models.EmailField(max_length=300, unique=True)
    




