from django.contrib import admin
from .models import Book, Category, Author
# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ['name', 'author_name']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
