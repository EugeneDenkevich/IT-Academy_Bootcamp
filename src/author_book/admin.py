from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'secondname', 'slug')
    list_display_links = ('id', 'firstname', 'secondname')
    prepopulated_fields = {'slug': ('firstname', 'secondname')}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
