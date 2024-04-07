from django.urls import path
from .views import list_books, book_detail

urlpatterns = [
    path('book_list', list_books),
    path('book_list/<int:product_id>', book_detail)
]
