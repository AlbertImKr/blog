from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'status', 'tags', 'category']
        widgets = {
            'title': forms.TextInput(
                    attrs={'required': True, 'id': 'con-name', 'name': 'name',
                           'type': 'text', 'class': 'form-control',
                           'placeholder': 'Post title'}),
            'content': forms.Textarea(
                    attrs={'class': 'form-control', 'rows': '10',
                           'placeholder': 'Add content'}),
            'tags': forms.SelectMultiple(
                    attrs={'class': 'form-control', 'rows': '1',
                           'placeholder': 'business, finance, health'}),
            'category': forms.Select(
                    attrs={'class': 'form-select',
                           'aria-label': 'Default select example'}),
            'status': forms.CheckboxInput(
                    attrs={'class': 'form-check-input', 'type': 'checkbox',
                           'id': 'postCHeck'}),
        }
