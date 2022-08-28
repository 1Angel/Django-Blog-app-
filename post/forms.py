from django import forms
from post.models import Post
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "imagen"]



class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username", "email", "password1", "password2"
        ]
