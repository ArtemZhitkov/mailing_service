from django import forms
from email_validator import validate_email, EmailNotValidError
from django.contrib.auth.forms import UserCreationForm
from .models import User

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.EmailField):
                field.widget.attrs.update({"class": "form-control", "type": "email"})
            elif isinstance(field, forms.ImageField):
                field.widget.attrs.update({"class": "form-control", "type": "file"})
            else:
                field.widget.attrs.update({"class": "form-control"})

class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone_number', 'area', 'password1', 'password2')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except EmailNotValidError as e:
            raise forms.ValidationError(str(e))
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен содержать только цифры.')
        return phone_number

class PasswordResetForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ['password1', 'password2']
        labels = {
            'password1': 'Новый пароль',
            'password2': 'Подтверждение нового пароля',
        }