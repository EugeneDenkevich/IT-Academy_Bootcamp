from django.test import TestCase

from .models import Book
from .forms import BookForm


class MyOnlyTestClass(TestCase):

    
    def test_book_create_spec_symb_true(self):
        d = {'title': 'Incredible Book 2'}
        form = BookForm(d)
        self.assertTrue(form.is_valid())

    def test_book_create_spec_symb_false(self):
        d = {'title': '!-Incredible Book-!'}
        form = BookForm(d)
        self.assertFalse(form.is_valid())

