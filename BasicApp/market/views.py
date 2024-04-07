from .models import Book
from django.http import JsonResponse
# Create your views here.


def list_books(request):
    books = Book.objects.all()
    json_products = []
    for book in books:
        json_products.append({
            "name": book.name,
            "page_count": book.page_count,
            "category": book.category,
            "author_name": book.author_name,
            "price": book.price,
            # "image": book.image
        }
        )
    return JsonResponse(json_products, safe=False)


def book_detail(request, product_id):
    book = Book.objects.get(pk=product_id)
    json_book = {
            "name": book.name,
            "page_count": book.page_count,
            "category": book.category,
            "author_name": book.author_name,
            "price": book.price,
            # "image": book.image
        }
    return JsonResponse(json_book, safe=False)
