from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
    context = {
        'title': 'Главная страница',
        'links': [
            ('writers', 'Писатели'),
            ('books', 'Топ лучших книг')
        ]
    }
    return render(request, 'writes/home.html', context)

def writers(request):
    context = {
        'title': 'Писатели',
        'writers': [
            {'name': 'Лев Толстой'},
            {'name': 'Александр Пушкин'},
            {'name': 'Федор Достоевский'}
        ]
    }
    return render(request, 'writes/writers.html', context)

def top_books(request):
    context = {
        'title': 'Топ лучших книг',
        'books': [
            {'title': 'Война и мир'},
            {'title': 'Евгений Онегин'},
            {'title': 'Преступление и наказание'}
        ]
    }
    return render(request, 'writes/books.html', context)