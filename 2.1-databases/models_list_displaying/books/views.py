from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_pages(request, pub_date):
    page = {}
    template = 'books/books_list.html'
    books = Book.objects.filter(pub_date=pub_date)
    previous_page = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date')
    next_page = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date')
    if previous_page:
        page['previous_page'] = previous_page[0]
    if next_page:
        page['next_page'] = next_page[0]
    context = {
        'books': books,
        'page': page,
    }
    return render(request, template, context)
