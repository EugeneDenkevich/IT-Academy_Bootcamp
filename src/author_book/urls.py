from django.urls import path

from . import views


urlpatterns = [
    path('', views.show_all, name='index'),
    path('book/<int:book_id>/<slug:book_slug>', views.show_book, name='show_book'),
    path('authors/<int:author_id>/<slug:author_slug>',
         views.show_author_and_his_books, name='show_author'),
    path('new-book', views.AddBookView.as_view(), name='add_book'),
    path('new-author', views.AddAuthorView.as_view(), name='add_author'),



    path('<int:book_id>/change_book',
         views.change_book, name='change_book'),
    path('<int:pk>/delete_book',
         views.BookDeleteView.as_view(), name='delete_book'),
    path('<int:author_id>/change_author',
         views.change_author, name='change_author'),
    path('<int:pk>/delete_author',
         views.del_author, name='delete_author'),
]
