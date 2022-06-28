from django.contrib import admin

from bookstore.models import Book, Author, Review


class BookInline(admin.TabularInline):
    model = Book
    extra = 0
    fields = ('title', 'released_year')
    show_change_link = True


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'age')
    list_filter = ('last_name',)
    fields = [('last_name', 'first_name', 'age')]
    search_fields = ['last_name']

    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'released_year', 'author')
    list_filter = ('title', 'author')
    search_fields = ['title', 'released_year']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'book', 'user')
    list_filter = ('book', 'user')
    search_fields = ['book__title', 'user__username']
    fieldsets = (
        (None, {
            'fields': ('user', 'book')
        }),
        ('Review', {
            'fields': ('title', 'review_text')
        }),
    )
