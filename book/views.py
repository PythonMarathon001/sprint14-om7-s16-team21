from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from book.models import Book
from order.models import Order

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

def filtered_books(request):
    book_objects = Book.objects.all()
    books_by_name = Book.objects.filter(name__startswith="book")

    for book in book_objects:
        pass

    context = {'book_objects': book_objects,
               'books_by_name': books_by_name,
               }
    return render(request, 'book/filtered_books.html', context)

class ID_BookView(generic.DetailView):
    model = Book
    template_name = 'book/id_book.html'


