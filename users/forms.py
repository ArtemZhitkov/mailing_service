from django import forms
from django.contrib.auth.forms import UserCreationForm
from email_validator import EmailNotValidError, validate_email

from .models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.EmailField):
                field.widget.attrs.update({"class": "form-control", "type": "email"})
            elif isinstance(field, forms.ImageField):
                field.widget.attrs.update({"class": "form-control", "type": "file"})
            elif isinstance(field, forms.BooleanField):
                field.widget.attrs.update({"class": "form-check-input"})
            else:
                field.widget.attrs.update({"class": "form-control"})


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "avatar", "phone_number", "area", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            validate_email(email)
        except EmailNotValidError as e:
            raise forms.ValidationError(str(e))
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number


class UserEditForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "first_name", "last_name", "avatar", "phone_number", "area")
        exclude = ("password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            validate_email(email)
        except EmailNotValidError as e:
            raise forms.ValidationError(str(e))
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number


class UserManagerEditForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ("is_active",)
