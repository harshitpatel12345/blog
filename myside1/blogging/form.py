from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comment,Blog,CustomUser

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content','image']

class BlogEditForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = '__all__'

class ProfileImageDeleteForm(forms.Form):
    confirm = forms.BooleanField(required=True, label="Confirm deletion")

