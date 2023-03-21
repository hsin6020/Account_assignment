import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_length(value):
    if not value:
        raise ValidationError('Username/Password cannot be empty.')
    if len(value) < 8:
        raise ValidationError('Username must be at least 8 characters long.')
    return value
        
def validate_pattern(value):
    if not re.search(r'\d', value):
        raise ValidationError('Password must contain at least one digit.')
    if not re.search(r'[a-z]', value):
        raise ValidationError('Password must contain at least one lowercase letter.')
    if not re.search(r'[A-Z]', value):
        raise ValidationError('Password must contain at least one uppercase letter.')
    return value