from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Book, Author
from .forms import AddAuthorForm, AddBookForm


def index(request):
    """Bookstore homepage view"""
    books = Book.objects.all()

    if request.method == "GET" and "search_text" in request.GET:
        search_text = request.GET['search_text']
        books = books.filter(title__icontains=search_text)

    return render(request, 'bookstore/index.html',
                  context={'books': books})


def book_detail(request, id):
    """Book detail view"""
    book = Book.objects.get(pk=id)

    return render(request, 'bookstore/book-detail.html',
                  context={'book': book})


def author_detail(request, id):
    """Author detail view"""
    author = Author.objects.get(pk=id)

    return render(request, 'bookstore/author-detail.html',
                  context={'author': author})


def author_book_list(request, id):
    """View returns all books of selected author"""
    author = Author.objects.get(pk=id)
    books = author.get_all_author_books()

    return render(request, 'bookstore/author-book-list.html',
                  context={'books': books, 'author': author})


def add_book(request):
    """View to add book to the bookstore"""
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bookstore:index'))
    else:
        form = AddBookForm()

    return render(request, 'bookstore/add-book.html', {'form': form})


def add_author(request):
    """View to add author to the bookstore"""
    if request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('bookstore:add_book'))
    else:
        form = AddAuthorForm()

    return render(request, 'bookstore/add-author.html', {'form': form})
