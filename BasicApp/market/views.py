from market.models import Book
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.core.paginator import Paginator


def list_books(request):
    try:
        books = Book.objects.filter().values_list('name', 'page_count', 'author', 'price', 'image', 'cover',  'category',)
    except Book.DoesNotExist:
        raise Http404("No Book matches the given query.")

    return JsonResponse(list(books), safe=False)


def book_detail(request, product_id):
    book = get_object_or_404(Book, pk=product_id)
    categories = book.category.all().values_list('name', flat=True)
    json_book = {
            "name": book.name,
            "page_count": book.page_count,
            "category": list(categories),
            "author_name": book.author.name if book.author else None,
            "price": book.price,
            "cover": book.get_cover_display()
        }
    return JsonResponse(json_book, safe=False)

def book_detailed_view(request, id):
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