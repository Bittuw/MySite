from django import forms
from .models import Consert
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            }),
        max_length=30, min_length=5, required=True, label='Login'
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': u'Иван',
            }),
        max_length=30, required=True, label='Firstname'
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': u'Иванов',
            }),
        max_length=30, required=True, label='Lastname'
    )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'me@gmail.com',
            }),
        required=True, max_length=254, label='E-mail'
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '*****'
            }),
        min_length=8, label='Password'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': '*****'
            }),
        min_length=8, label=u'Repeat password'
    )

    def clean_username(self):
        username = self.cleaned_data.get('username', '')

        try:
            u = User.objects.get(username=username)
            raise forms.ValidationError('Such user already exists')
        except User.DoesNotExist:
            return username

    def clean_password2(self):
        pass1 = self.cleaned_data.get('password1', '')
        pass2 = self.cleaned_data.get('password2', '')

        if pass1 != pass2:
            raise forms.ValidationError('Passwords do not match')

    def save(self):
        data = self.cleaned_data
        password = data.get('password1')
        u = User()

        u.username = data.get('username')
        u.password = make_password(password)
        u.email = data.get('email')
        u.first_name = data.get('first_name')
        u.last_name = data.get('last_name')
        u.is_active = True
        u.is_superuser = False
        u.save()

        return authenticate(username=u.username, password=password)


class SigninForm(forms.Form):
    login = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username', }
        ),
        max_length=30,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password', }
        ),
    )

    def clean(self):
        data = self.cleaned_data
        user = authenticate(
            username=data.get('login', ''),
            password=data.get('password', '')
            )

        if user is not None:
            if user.is_active:
                data['user'] = user
            else:
                raise forms.ValidationError('The user is not active')
        else:
            raise forms.ValidationError('Wrong username or password')


class ConsertForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Name',
            }),
        max_length=30, min_length=5, required=True, label='Name'
    )
    theatre = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Theatre',
            }),
        max_length=40, min_length=20,  required=True, label='Theatre'
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Description',
            }),
        max_length=100, min_length=20,  required=True, label='Description'
    )
    time = forms.DateTimeField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Time',
            }),
        required=True, label='Time',
        input_formats=[
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%d %H:%M',
        ]
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', }),
        required=False, label='Image'
    )

    def fill_object(self):
        return Consert.objects.create(
            name=self.cleaned_data['name'],
            theatre=self.cleaned_data['theatre'],
            description=self.cleaned_data['description'],
            time=self.cleaned_data['time']
        )
