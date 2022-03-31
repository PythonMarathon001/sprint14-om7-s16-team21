from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from book.models import Book
def home(request):
    return HttpResponse('home')
def show_all(request):
    #return HttpResponse(print(Book.get_all()))
    #return HttpResponse(Book.objects.all())
    return HttpResponse(Book.objects.get)