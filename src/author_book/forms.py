from django.forms import ModelForm, TextInput, CheckboxInput
from .models import *
from django.core.exceptions import ValidationError


# Переделать в формсет и добавить в форму авторов?
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
        ]

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Серый волк и Красная шапочка',
                'lable': 'Книга'
            }),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        forbit = '!@#$%^&*()_+-=<>/\,`~|.][{}'
        for i in forbit:
            for j in title:
                if i == j:
                    raise ValidationError(
                        'В названии книги не должно быть спецсимволов!')
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

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']
        forbit = '1234567890!@#$%^&*()_+-=<>/\,`~|.][{}'
        for i in forbit:
            for j in firstname:
                if i == j:
                    raise ValidationError(
                        'В имени не должно быть спецсимволов!')
        return firstname

    def clean_secondname(self):
        secondname = self.cleaned_data['secondname']
        forbit = '1234567890!@#$%^&*()_+-=<>/\,`~|.][{}'
        for i in forbit:
            for j in secondname:
                if i == j:
                    raise ValidationError(
                        'В фамилии не должно быть спецсимволов!')
        return secondname


