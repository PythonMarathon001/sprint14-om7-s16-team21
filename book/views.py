from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.views import generic

from book.models import Book

# Create your views here.

def index(request):
    return render(request, 'book/index.html')

def allbooks(request):
    book_objects = Book.objects.all()
    context = {'book_objects': book_objects}
    return render(request, 'book/allbooks.html', context)

# def id_book(request, book_id):
#     try:
#         book = Book.objects.get(pk=book_id)
#     except Book.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'book/', )

class ID_BookView(generic.DetailView):
    model = Book
    template_name = 'book/id_book.html'


