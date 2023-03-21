from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        error_messages = {
            'username': {
                'max_length': 'Username is too long, it cannot be longer than 32 characters.',
            },
            'password': {
                'max_length': 'Password is too long, it cannot be longer than 32 characters.',
            }
        }