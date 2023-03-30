from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=200, verbose_name='Имя')
    secondname = models.CharField(max_length=200, verbose_name='Фамилия')
    book = models.ManyToManyField('Book',
                                  blank=True,
                                  related_name='authors')

    def __str__(self) -> str:
        return f'{self.firstname} {self.secondname}'


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'
