
from django import forms
# models
from apps.models.models import Profiles, Area


class LoginForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ('name', 'password')
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
            'password': forms.PasswordInput(
                attrs={'placeholder': 'Password'}
            )
        }


class SignUpForm(forms.ModelForm):
    area = forms.ModelChoiceField(queryset=Area.objects.values_list('name', flat=True))

    class Meta:
        model = Profiles
        fields = ('name', 'password', 'email', 'area', 'department')
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Username'}
            ),
            'password': forms.TextInput(
                attrs={'placeholder': 'Password'}
            ),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email',
                       'type': 'email'}
            ),
        }


