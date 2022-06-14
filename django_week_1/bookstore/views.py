from django.shortcuts import render
from django.http import Http404

from .helper_functions import get_object_by_id_or_404


books = [{
        'id': 1,
        'title': 'Learning Python, 5th Edition',
        'released_year': 2013,
        'description': '''Get a comprehensive, in-depth introduction to the
        core Python language with this hands-on book. Based on author Mark
        Lutz’s popular training course, this updated fifth edition will help
        you quickly write efficient, high-quality code with Python. It’s an
        ideal way to begin, whether you’re new to programming or a professional
        developer versed in other languages.''',
        'author_id': 1,
        },

        {
        'id': 2,
        'title': 'Python Pocket Reference, 5th Edition',
        'released_year': 2014,
        'description': '''Updated for both Python 3.4 and 2.7, this convenient
        pocket guide is the perfect on-the-job quick reference. You will find
        concise, need-to-know information on Python types and statements,
        special method names, built-in functions and exceptions, commonly used
        standard library modules, and other prominent Python tools. The handy
        index lets you pinpoint exactly what you need.''',
        'author_id': 1,
        },

        {
        'id': 3,
        'title': 'Programming Python, 4th Edition',
        'released_year': 2010,
        'description': '''If you've mastered Python's fundamentals, you're
        ready to start using it to get real work done. Programming Python
        will show you how, with in-depth tutorials on the language's
        primary application domains: system administration, GUIs, and the
        Web. You'll also explore how Python is used in databases,
        networking, front-end scripting layers, text processing, and more.
        This book focuses on commonly used tools and libraries to give you
        a comprehensive understanding of Python’s many roles in practical,
        real-world programming.''',
        'author_id': 1,
        },

        {
        'id': 4,
        'title': 'Fluent Python, 2nd Edition',
        'released_year': 2022,
        'description': '''Python’s simplicity lets you become productive
        quickly, but often this means you aren’t using everything it has to
        offer. With the updated edition of this hands-on guide, you’ll
        learn how to write effective, modern Python 3 code by leveraging
        its best ideas.''',
        'author_id': 2,
        },

        {
        'id': 5,
        'title': 'Python vs. Go',
        'released_year': 2018,
        'description': '''Comparing Python with Go is a bit like comparing an
        SUV with a sports car: they were created to serve different needs.
        Thanks to their simple syntax and careful design, you will probably
        find Python and Go easier to learn and use than other mainstream
        languages that you might have already studied. Given their gentle
        learning curve and phenomenal growth in several fields, getting to
        know them is a sound investment now.''',
        'author_id': 2,
        },

        {
        'id': 6,
        'title': 'Learning Go',
        'released_year': 2021,
        'description': '''Go is rapidly becoming the preferred language for
        building web services. While there are plenty of tutorials
        available that teach Go's syntax to developers with experience in
        other programming languages, tutorials aren't enough. They don't
        teach Go's idioms, so developers end up recreating patterns that
        don't make sense in a Go context. This practical guide provides the
        essential background you need to write clear and idiomatic Go.''',
        'author_id': 3,
        },

        {
        'id': 7,
        'title': 'Building Microservices, 2nd Edition',
        'released_year': 2021,
        'description': '''As organizations shift from monolithic applications
        to smaller, self-contained microservices, distributed systems have
        become more fine-grained. But developing these new systems brings
        its own host of problems. This expanded second edition takes a
        holistic view of topics that you need to consider when building,
        managing, and scaling microservices architectures.''',
        'author_id': 4,
        },

        {
        'id': 8,
        'title': 'Head First Design Patterns, 2nd Edition',
        'released_year': 2020,
        'description': '''You know you don't want to reinvent the wheel, so you
        look to Design Patterns: the lessons learned by those who've faced
        the same software design problems. With Design Patterns, you get to
        take advantage of the best practices and experience of others so
        you can spend your time on something more challenging. Something
        more fun. This book shows you the patterns that matter, when to use
        them and why, how to apply them to your own designs, and the
        object-oriented design principles on which they're based. Join
        hundreds of thousands of developers who've improved their
        object-oriented design skills through Head First Design
        Patterns.''',
        'author_id': 5,
        },
        ]

authors = [{
        'id': 1,
        'first_name': 'Mark',
        'last_name': 'Lutz',
        'age': 81,
        },

        {
        'id': 2,
        'first_name': 'Luciano',
        'last_name': 'Ramalho',
        'age': 59,
        },

        {
        'id': 3,
        'first_name': 'Jon',
        'last_name': 'Bodner',
        'age': 54,
        },

        {
        'id': 4,
        'first_name': 'Sam',
        'last_name': 'Newman',
        'age': 48,
        },

        {
        'id': 5,
        'first_name': 'Eric',
        'last_name': 'Freeman',
        'age': 50,
        },
        ]


def index(request):
    return render(request, 'bookstore/index.html',
                  context={'books': books, 'authors': authors})


def book_detail(request, id):
    book = get_object_by_id_or_404(id, books)

    author = get_object_by_id_or_404(book['author_id'], authors)

    return render(request, 'bookstore/book-detail.html',
                  context={'book': book, 'author': author})


def author_detail(request, id):
    author = get_object_by_id_or_404(id, authors)

    return render(request, 'bookstore/author-detail.html',
                  context={'author': author})


def author_book_list(request, id):
    author = get_object_by_id_or_404(id, authors)

    book_list = []
    for book in books:
        if book['author_id'] == id:
            book_list.append(book)

    return render(request, 'bookstore/author-book-list.html',
                  context={'book_list': book_list, 'author': author})
