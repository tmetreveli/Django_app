from django.urls import path
from .views import list_books, book_detail, show, book_detailed_view

app_name = 'market'

urlpatterns = [
    path('book_list', list_books),
    path('book_list/<int:product_id>', book_detail),
    path('', show),
    path('details/<int:id>', book_detailed_view, name='book_detailed_view')
]
