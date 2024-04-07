from django.contrib import admin
from .models import Book
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['name', 'author_name']
