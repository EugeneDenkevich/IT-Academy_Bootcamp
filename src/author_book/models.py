from django.db import models
from django.urls import reverse
from pytils.translit import slugify


class Author(models.Model):
    firstname = models.CharField(max_length=125, verbose_name='Имя')
    secondname = models.CharField(max_length=125, verbose_name='Фамилия')
    book = models.ManyToManyField('Book',
                                  blank=True,
                                  related_name='authors')
    slug = models.SlugField(db_index=True, max_length=255, null=False)


    def __str__(self) -> str:
        return f'{self.firstname} {self.secondname}'
    
    def get_absolute_url(self):
        return reverse('show_author', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.firstname} {self.secondname}')
        return super().save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название книги')
    created_at = models.DateTimeField(auto_now_add=True)
    has_authors = models.CharField(max_length=1, null=True)
    slug = models.SlugField(db_index=True, max_length=255, null=False)

    def __str__(self) -> str:
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('show_book', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}')
        return super().save(*args, **kwargs)