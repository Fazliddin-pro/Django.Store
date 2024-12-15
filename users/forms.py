from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User()
        fields = ['username', 'password']

    username = forms.CharField()
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'country',
            'address',
            'password1',
            'password2'
        )
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    country = forms.CharField(required=False, empty_value='Uzbekistan')
    address = forms.CharField(required=False)
    password1 = forms.CharField()
    password2 = forms.CharField()


class CheckoutForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'country',
            'address',
        )

    image = forms.ImageField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    phone_number = forms.CharField()
    country = forms.CharField(required=False, empty_value='Uzbekistan')
    address = forms.CharField(required=False)
