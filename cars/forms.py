from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Comment

class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label="Login", widget=forms.TextInput())
    email = forms.EmailField(label="Email", widget=forms.EmailInput())
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput(),)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    

class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label="Login", widget=forms.TextInput())# для использования css в формах TextInput(attrs={'class': 'class_name'})
    password = forms.CharField(label="Password", widget=forms.PasswordInput())


class CommentForm(forms.ModelForm):
    
    header = forms.CharField(label="Header", widget=forms.TextInput(attrs={'class': 'form-header'}))
    body = forms.CharField(label="Body", widget=forms.Textarea(attrs={'class': 'form-body'}))

    class Meta:
        model = Comment
        fields = ('header', 'body')
