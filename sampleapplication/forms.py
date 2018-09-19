from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "username"
            }
        ))
    password = forms.CharField(widget = forms.PasswordInput(
        attrs = {
            "class": "form-control",
            "placeholder": "password"
        }
    ))

class RegisterForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "username"
            }
        ))
    email = forms.CharField(widget = forms.EmailInput(
            attrs = {
                "class": "form-control",
                "placeholder": "EmailId"
            }
        ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
                "class": "form-control",
                "placeholder": "Password"
            }
    ))

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs = {
                "class": "form-control",
                "placeholder": "Confirm password"
            })
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        print(email)
        qs = User.objects.filter(email=email)
        print(qs.exists())
        if qs.exists():
            raise forms.ValidationError("email is already exists")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password2 != password:
            raise forms.ValidationError("password must match.")
        return data