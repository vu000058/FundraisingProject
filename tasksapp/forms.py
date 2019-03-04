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

EVENT_TYPE = (
    ("Donation", "Donation"),
    ("Deduction", "Deduction")
)


class SectionForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput())
    year = forms.ChoiceField(choices=YEAR_CHOICES, label="Year", widget=forms.Select(), required=True)
    term = forms.ChoiceField(choices=TERM_CHOICES, label="Term",  widget=forms.Select(), required=True)

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

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

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError({
    #             'email': 'Email already existed'
    #         })
    #
    #     password = self.cleaned_data.get('password')
    #     confirm_password = self.cleaned_data.get('confirm_password')
    #     if confirm_password != password:
    #         raise forms.ValidationError({
    #             'password': 'Passwords mismatched'
    #         })
    #     return self.cleaned_data


class EventForm(forms.Form):
    name = forms.CharField(label="Event Name", widget=forms.TextInput())
    description = forms.CharField(label="Description", widget=forms.Textarea(attrs={'rows':3}))
    type = forms.ChoiceField(choices=EVENT_TYPE, label="Type", widget=forms.RadioSelect())
    amount = forms.CharField(label="Amount",  widget=forms.TextInput(), required=True)

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != 'type':
                visible.field.widget.attrs['class'] = 'form-control'


class ChangePasswordForm(forms.Form):
    password = forms.CharField(label="Current Password", widget=forms.PasswordInput())
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())


    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError("New passwords do not match.")


