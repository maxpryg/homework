from django.urls import path

from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('author/<int:id>/', views.author_detail, name='author_detail'),
    path('author/<int:id>/books/', views.author_book_list,
         name='author_book_list'),
    path('add_book', views.add_book, name='add_book'),
    path('add_author', views.add_author, name='add_author'),
]
