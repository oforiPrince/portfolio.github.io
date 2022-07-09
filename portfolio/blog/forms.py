from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'owner', 'body', 'tags', 'main_image', 'published')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'owner': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select an Author'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control', }),
            'main_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check'}),
        }
