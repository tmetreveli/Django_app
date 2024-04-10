from .models import Book
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core import serializers


def list_books(request):
    try:
        books = Book.objects.filter().values_list('name', 'page_count', 'category', 'author_name', 'price', 'image')
    except Book.DoesNotExist:
        raise Http404("No Book matches the given query.")

    return JsonResponse(list(books), safe=False)


def book_detail(request, product_id):
    book = get_object_or_404(Book, pk=product_id)
    json_book = {
            "name": book.name,
            "page_count": book.page_count,
            "category": book.category,
            "author_name": book.author_name,
            "price": book.price,
        }
    return JsonResponse(json_book, safe=False)

def show(request):
    page = int(request.GET.get('page', 1))
    page_size = 3
    books = Book.objects.all()[(page - 1) * page_size: page * page_size]
    return render(request, "index.html", {"books": books})