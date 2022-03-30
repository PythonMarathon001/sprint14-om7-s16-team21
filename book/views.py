from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from book.models import Book

# Create your views here.

def index(request):
    return render(request, 'book/index.html')

def allbooks(request):
    book_objects = Book.objects.all()
    context = {'book_objects': book_objects}
    return render(request, 'book/allbooks.html', context)
