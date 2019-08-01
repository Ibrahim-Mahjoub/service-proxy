from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class SPUser(AbstractUser):
    """
    A custom user model. (inherits from default django user model)
    """
    pass
