from django.core.validators import MinLengthValidator
from django.db import models

from .validators import validate_pattern

class Account(models.Model):
    username = models.CharField(
        max_length=32,
        unique=True,
        validators=[MinLengthValidator(3, "Username must be at least 3 characters long.")],
    )
    password = models.CharField(
        max_length=32,
        validators=[validate_pattern, 
                    MinLengthValidator(8, "Password must be at least 8 characters long.")
        ],
    )