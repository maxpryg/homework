from django import forms

from .models import Book, Author, Review


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'age']



class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'released_year', 'description']


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'review_text']
