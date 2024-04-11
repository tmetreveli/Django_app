from .models import Book
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.paginator import Paginator


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

def book_detailed_view(request, id):
    # product_id = request.GET.get('id')
    book = get_object_or_404(Book, pk=id)
    return render(request, "detail_book.html", {"book": book})
def show(request):
    queryset = Book.objects.all()
    paginator = Paginator(queryset, 2)
    print(paginator.num_pages)
    page_num = int(request.GET.get('page', 1))
    page = paginator.get_page(number=page_num)
    print(page.has_next())
    return render(request, "index.html", {"page": page})