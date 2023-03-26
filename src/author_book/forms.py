from django.forms import ModelForm, TextInput, CheckboxInput
from .models import *


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
        ]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги',
            }),
        }


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = [
            'firstname',
            'secondname',
        ]

        widgets = {
            'firstname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'secondname': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
        }
