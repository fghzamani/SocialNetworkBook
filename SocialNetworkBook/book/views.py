from django.shortcuts import render
from .models import Book


# Create your views here.


def show_book(r='s'):
    context = Book.objects.all()
    data = {
        'context': context
    }
    return render(r, 'index.html', data)
