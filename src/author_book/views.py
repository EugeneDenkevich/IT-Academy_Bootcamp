from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import DeleteView
from django.db.models import Model
from django.views.generic.edit import FormView, CreateView


from .models import Author, Book
from .forms import BookForm, AuthorForm


# New
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


# Old

def check_book_title(full_request):
    title = ''.join(dict(full_request)['title'])
    forbit = '!@#$%^&*()_+-=<>/\,`~|.][{}'
    for i in forbit:
        for j in title:
            if i == j:
                return False

    return True


def check_fullname(full_request):
    f_name = ''.join(dict(full_request)['firstname'])
    s_name = ''.join(dict(full_request)['secondname'])
    forbit = '1234567890!@#$%^&*()_+-=<>/\,`~|.][{}'
    for i in forbit:
        for j in f_name:
            if i == j:
                return False
        for j in s_name:
            if i == j:
                return False

    return True


def get_attributes(request_post):
    request_dict = dict(request_post)
    res = {k: request_dict[k] for k in request_dict if ("==>") in k}

    return res


def get_add_process(copmlete_dict: dict,
                    active_model: Model,
                    passive_model: Model):
    ids_dict = copmlete_dict.values()
    objects = []
    for id in ids_dict:
        pk = int(''.join(id))
        objects.append(active_model.objects.get(pk=pk))
    instance = passive_model.objects.all().order_by('-id')[0]

    return objects, instance


def get_update_process(copmlete_dict: dict,
                       active_model: Model):
    ids = copmlete_dict.values()
    objects = []
    for id in ids:
        pk = int(''.join(id))
        objects.append(active_model.objects.get(pk=pk))

    return objects


def show_book(request, id_book):
    book = Book.objects.get(pk=id_book)
    authors = book.authors.all()
    context = {
        'book': book,
        'authors': authors
    }

    return render(request, 'book.html', context=context)


def get_fullcontext():
    authors = Author.objects.all().order_by('-id')
    books = Book.objects.all().order_by('-id')

    return {'authors': authors, 'books': books}


def show_all(request):
    books = Book.objects.all()
    # for book in books:
    #     if list(book.authors.all()) == []:
    #         book.delete()
    context = get_fullcontext()
    return render(request, 'authors_books.html', context=context)


def show_author_and_his_books(request, id_author):
    author = get_object_or_404(Author, pk=id_author)
    try:
        books = get_list_or_404(Book, authors=author)
    except:
        books = None
    context = {
        'author': author,
        'books': books
    }

    return render(request, 'author.html', context=context)


# def add_author(request):
#     error = None
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         books_dict = get_attributes(request.POST)
#         if check_fullname(request.POST):
#             if form.is_valid():
#                 form.save()
#                 item, box = get_add_process(books_dict, Book, Author)
#                 box.book.add(*item)
#                 return redirect('index')
#         else:
#             error = 'Нельзя использовать спецсимволы и цифры в имени и фамилии'

#     context = get_fullcontext()
#     form = AuthorForm()
#     data = {
#         'books': context['books'],
#         'form': form,
#         'error': error
#     }

#     return render(request, 'add_author.html', context=data)


def change_book(request, book_id):
    error_authors = None
    error_title = None
    if request.method == 'POST':
        form = BookForm(request.POST)
        authors_dict = get_attributes(request.POST)
        if check_book_title(request.POST):
            if authors_dict:
                if form.is_valid():
                    book = Book.objects.get(pk=book_id)
                    book.title = ''.join(dict(request.POST)['title'])
                    book.save()
                    authors = get_update_process(authors_dict, Author)
                    book.authors.clear()
                    book.authors.add(*authors)
                    return redirect('index')
            else:
                error_authors = 'Нужно указать хотя бы одного автора'
        else:
            error_title = 'Название не должно содержать спецсимволы'

    book = Book.objects.get(pk=book_id)
    form = BookForm()
    authors = Author.objects.all()
    book_authors = book.authors.all()
    context = {
        'form': form,
        'book': book,
        'authors': authors,
        'book_authors': book_authors,
        'error_authors': error_authors,
        'error_title': error_title
    }

    return render(request, 'change_book.html', context=context)


def change_author(request, author_id):
    error = None
    if request.method == 'POST':
        if check_fullname(request.POST):
            form = AuthorForm(request.POST)
            request_dict = dict(request.POST)
            print('--->>>', request_dict)
            books_dict = get_attributes(request.POST)
            if form.is_valid():
                author = Author.objects.get(pk=author_id)
                author.firstname = ''.join(request_dict['firstname'])
                author.secondname = ''.join(request_dict['secondname'])
                author.save()
                books = get_update_process(books_dict, Book)
                author.book.clear()
                author.book.add(*books)
                return redirect('index')
        else:
            error = 'Нельзя использовать спецсимволы и цифры в имени и фамилии'

    author = Author.objects.get(pk=author_id)
    form = AuthorForm()
    books = Book.objects.all()
    authors_book = author.book.all()
    context = {
        'form': form,
        'author': author,
        'books': books,
        'authors_book': authors_book,
        'error': error
    }

    return render(request, 'change_author.html', context=context)


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'
    template_name = 'delete_book.html'


def del_author(request, pk):
    author = Author.objects.get(pk=pk)
    books = author.book.all()
    for book in books:
        if author in book.authors.all():
            if list(book.authors.exclude(id=author.id)) == []:
                book.delete()
    Author.objects.get(pk=pk).delete()
    return redirect('index')
