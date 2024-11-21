# forms.py
from django import forms

class PasswordUpdateForm(forms.Form):
    password = forms.CharField(
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput,
        label='Contraseña'
    )
    confirm_password = forms.CharField(
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput,
        label='Confirmar Contraseña'
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
