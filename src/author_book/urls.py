from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book/<int:pk>',
         views.BookDetailView.as_view(), name='show_book'),
    path('authors/<int:pk>',
         views.AuthorDetailView.as_view(), name='show_author'),
    path('new-book', views.AddBookView.as_view(), name='add_book'),
    path('new-author', views.AddAuthorView.as_view(), name='add_author'),
    path('<int:pk>/change_book',
         views.BookUpdateView.as_view(), name='change_book'),
    path('<int:pk>/delete_book',
         views.BookDeleteView.as_view(), name='delete_book'),
    path('<int:pk>/change_author',
         views.AuthorUpdateView.as_view(), name='change_author'),
    path('<int:pk>/delete_author',
         views.AuthorDeleteView.as_view(), name='delete_author'),
]
