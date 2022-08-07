from django import forms
from .models import Blog, Tag, Category


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'owner', 'body', 'category', 'tags', 'main_image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'class': 'form-control form-control-sm'}),
            'owner': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select an Author', 'class': 'form-control form-control-sm'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body', 'class': 'form-control form-control-sm'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select a Category', 'class': 'form-control form-control-sm'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control', 'class': 'form-control form-control-sm'}),
            'main_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*', 'class': 'form-control form-control-sm'}),
        }
