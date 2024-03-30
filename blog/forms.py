from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Blog

class UserSignUpForm(UserCreationForm):
    password2 = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}),label="Re-Enter Password ")
    password1 = forms.CharField(widget=forms.PasswordInput(attrs = {"class":"form-control"}),label="Password ")
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email"]
        widgets = {"username": forms.TextInput(attrs = {"class":"form-control"}),
                  "first_name": forms.TextInput(attrs = {"class":"form-control"}),
                  "last_name": forms.TextInput(attrs = {"class":"form-control"}),
                  "email": forms.TextInput(attrs = {"class":"form-control"})}
        
class UserLogInForm(AuthenticationForm):
    class Meta:
        fields = ["username", "password"]
        widgets = {"username": forms.TextInput(attrs = {"class":"form-control"}),
                   "password": forms.PasswordInput(attrs = {"class":"form-control"})}
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "blog"]