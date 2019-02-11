from django import forms
from django.contrib.auth.models import User

TERM_CHOICES = (
    ("Fall", "Fall"),
    ("Winter", "Winter"),
    ("Spring", "Spring")
)

YEAR_CHOICES = (
    (2019, 2019),
    (2020, 2020),
    (2021, 2021),
    (2022, 2022),
    (2023, 2023),
    (2024, 2024),
    (2025, 2025),
    (2026, 2027),
    (2028, 2028),
    (2029, 2029)
)


class SectionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    year = forms.ChoiceField(choices=YEAR_CHOICES, label="Year", widget=forms.Select(), required=True)
    term = forms.ChoiceField(choices=TERM_CHOICES, label="Term",  widget=forms.Select(), required=True)


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError({
                'email': 'Email already existed'
            })

        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if confirm_password != password:
            raise forms.ValidationError({
                'password': 'Passwords mismatched'
            })
        return self.cleaned_data


