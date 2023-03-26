from django.urls import path

from . import views


urlpatterns = [
    path('', views.show_all, name='index'),
    path('book/<int:id_book>', views.show_book, name='show_book'),
    path('author/<int:id_author>',
         views.show_author_and_his_books, name='show_author'),
    path('book/add_book', views.add_book, name='add_book'),
    path('author/add_author', views.add_author, name='add_author'),
    path('book/<int:book_id>/change_book',
         views.change_book, name='change_book'),
    path('book/<int:pk>/delete_book',
         views.BookDeleteView.as_view(), name='delete_book'),
    path('author/<int:author_id>/change_author',
         views.change_author, name='change_author'),
    path('author/<int:pk>/delete_author',
         views.del_author, name='delete_author'),
]
