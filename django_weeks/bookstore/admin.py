from django.contrib import admin

from bookstore.models import Book, Author, Review


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Review)
