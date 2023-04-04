from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, HttpResponseRedirect
from django.views.generic import DeleteView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Author, Book
from .forms import BookForm, AuthorForm


class IndexView(ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for book in self.get_queryset():
            if not book.authors.exists():
                book.has_authors = None
                book.save()
            else:
                book.has_authors = 1
                book.save()
        context['authors'] = Author.objects.all().order_by('-id')
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = self.get_object().authors.all()
        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.get_object().book.all()
        return context


class AddBookView(CreateView):
    form_class = BookForm
    success_url = '/'
    template_name = 'add_book.html'

    def get_context_data(self, **kwargs):
        authors = Author.objects.all()
        kwargs['authors'] = authors
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        request_dict = self.request.POST
        *authors_pks, = {k: request_dict[k] for k in request_dict if (
            "==>author_") in k}.values()
        if authors_pks == []:
            form = BookForm()
            authors = Author.objects.all()
            context = {
                'author_error': 'У книги должен быть хотя бы один автор',
                'authors': authors,
                'form': form,
            }
            return render(self.request, 'add_book.html', context)
        book = form.save(commit=False)
        book.save()
        book.authors.add(*(Author.objects.get(pk=pk) for pk in authors_pks))
        return super().form_valid(form)


class AddAuthorView(CreateView):
    form_class = AuthorForm
    success_url = '/'
    template_name = 'add_author.html'

    def get_context_data(self, **kwargs):
        books = Book.objects.all()
        kwargs['books'] = books
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        request_dict = self.request.POST
        *books_pks, = {k: request_dict[k] for k in request_dict if (
            "==>book_") in k}.values()
        author = form.save(commit=False)
        author.save()
        author.book.add(*(Book.objects.get(pk=pk) for pk in books_pks))
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'change_book.html'
    error_authors = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book_authors = self.get_object().authors.all()
        context['authors'] = Author.objects.all()
        context['book_authors'] = book_authors
        context['error_authors'] = self.error_authors
        return context

    def form_valid(self, form):
        request_dict = self.request.POST
        *authors_pks, = {k: request_dict[k] for k in request_dict if (
            "==>author_") in k}.values()
        if authors_pks == []:
            self.error_authors = 'У книги должен быть хотя бы один автор'
            return super(BookUpdateView, self).form_invalid(form)
        book = form.save(commit=False)
        book.save()
        book.authors.clear()
        book.authors.add(*(Author.objects.get(pk=pk) for pk in authors_pks))
        book.has_authors = 1
        book.save()
        return super().form_valid(form)


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'change_author.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_book = self.get_object().book.all()
        context['books'] = Book.objects.all()
        context['authors_book'] = author_book
        return context

    def form_valid(self, form):
        request_dict = self.request.POST
        *books_pks, = {k: request_dict[k] for k in request_dict if (
            "==>book_") in k}.values()
        author = form.save(commit=False)
        author.save()
        author.book.clear()
        author.book.add(*(Book.objects.get(pk=pk) for pk in books_pks))
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'
    template_name = 'delete_book.html'


class AuthorDeleteView(DeleteView):
    model = Author
    success_url = '/'
    template_name = 'delete_author.html'
