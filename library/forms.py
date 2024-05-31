from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_of_death': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'pub_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }


