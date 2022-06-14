from django.shortcuts import render

from .helper_functions import get_object_by_id_or_404
from .data import books, authors


def index(request):
    """Bookstore homepage view"""

    return render(request, 'bookstore/index.html',
                  context={'books': books, 'authors': authors})


def book_detail(request, id):
    """Book detail view"""

    book = get_object_by_id_or_404(id, books)

    author = get_object_by_id_or_404(book['author_id'], authors)

    return render(request, 'bookstore/book-detail.html',
                  context={'book': book, 'author': author})


def author_detail(request, id):
    """Author detail view"""

    author = get_object_by_id_or_404(id, authors)

    return render(request, 'bookstore/author-detail.html',
                  context={'author': author})


def author_book_list(request, id):
    """View returns all books of selected author"""

    author = get_object_by_id_or_404(id, authors)

    book_list = []
    for book in books:
        if book['author_id'] == id:
            book_list.append(book)

    return render(request, 'bookstore/author-book-list.html',
                  context={'book_list': book_list, 'author': author})
