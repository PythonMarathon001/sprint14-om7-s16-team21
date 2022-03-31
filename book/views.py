from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from book.models import Book
def home(request):
    return render(request, 'home.html')
def show_all(request):
    #return HttpResponse(Book.objects.all() правильно
    showall = Book.objects.all()
    return render(request, 'showall.html',{'showall': showall})

