from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from book.models import Book
from order.models import Order
from author.models import Author

# Create your views here.

def index(request):
    return render(request, 'book/index.html')

def allbooks(request):
    book_objects = Book.objects.all()
    order_objects = Order.objects.all()

    orders_book_id = []
    unordered_books_id = []
    for order in order_objects:
        orders_book_id.append(order.book.id)
    for book in book_objects:
        if book.id not in orders_book_id:
            unordered_books_id.append(book.id)

    context = {'book_objects': book_objects,
               'unordered_books_id': unordered_books_id,
               }
    return render(request, 'book/allbooks.html', context)

class ID_BookView(generic.DetailView):
    model = Book
    template_name = 'book/id_book.html'

def filtered_books(request):

    book_objects = Book.objects.all()
    books_by_name = book_objects.filter(name__startswith="book")
    books_by_description = book_objects.filter(description__icontains="adventures")
    books_by_author = book_objects.filter(authors__name__contains="M")

    user_id = 222
    orders_by_user_id = Order.objects.filter(user_id=user_id)

    author_id = 2
    books_by_author_id = book_objects.filter(authors__id=author_id)


    for book in book_objects:
        pass

    context = {'book_objects': book_objects,
               'books_by_name': books_by_name,
               'books_by_description': books_by_description,
               'books_by_author': books_by_author,
               # 'books_by_given_id': books_by_given_id,
               'orders_by_user_id': orders_by_user_id,
               'user_id': user_id,
               'books_by_author_id': books_by_author_id,
               'author_id': author_id,

               }
    return render(request, 'book/filtered_books.html', context)


def ordered_books_count_ascending(request):
    book_objects = Book.objects.all().order_by('count')
    # book_objects = Book.objects.filter(count__gt=5) #greater than 5

    context = {'book_objects': book_objects}
    return render(request, 'book/ordered_books.html', context)


def ordered_books_count_descending(request):
    book_objects = Book.objects.all().order_by('-count')

    context = {'book_objects': book_objects}
    return render(request, 'book/ordered_books.html', context)


def ordered_books_name_ascending(request):
    book_objects = Book.objects.all().order_by('name')

    context = {'book_objects': book_objects}
    return render(request, 'book/ordered_books.html', context)


def ordered_books_name_descending(request):
    book_objects = Book.objects.all().order_by('-name')

    context = {'book_objects': book_objects}
    return render(request, 'book/ordered_books.html', context)




