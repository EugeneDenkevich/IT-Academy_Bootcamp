from django.forms import ModelForm, TextInput, CheckboxInput
from .models import *
from django.core.exceptions import ValidationError


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

    def clean_title(self):
        title = self.cleaned_data['title']
        forbit = '!@#$%^&*()_+-=<>/\,`~|.][{}'
        for i in forbit:
            for j in title:
                if i == j:
                    raise ValidationError(
                        'В названии не должно быть спецсимволов!')

        return title


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
