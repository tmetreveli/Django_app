from django.db import models
from django.utils.translation import gettext_lazy as _
from market.choices import CATEGORY_CHOICES, COVER_CHOICES


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Author name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Category(models.Model):
    name = models.CharField(max_length=11, choices=CATEGORY_CHOICES, default='PAPERBACK', verbose_name=_("Category name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

# Create your models here.
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Book Author"))
    category = models.ManyToManyField(Category, default='undefined', verbose_name=_("Book Category"))
    name = models.CharField(max_length=255, verbose_name=_("Book title"))
    page_count = models.IntegerField(verbose_name=_("Page Count"))
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=_("Price"))
    image = models.ImageField(upload_to='images/', verbose_name=_("Image"))
    cover = models.CharField(max_length=9, choices=COVER_CHOICES, default='PAPERBACK', verbose_name=_("Book cover"))
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


