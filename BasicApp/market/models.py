from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('FANTASY', 'fantasy'),
        ('ROMANCE', 'romance'),
        ('DOCUMENTARY', 'documentary'),
        ('UNDEFINED', 'undefined')
    ]
    name = models.CharField(max_length=11, choices=CATEGORY_CHOICES, default='PAPERBACK')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

# Create your models here.
class Book(models.Model):
    COVER_CHOICES = [
            ('PAPERBACK', 'Paperback'),
            ('HARDCOVER', 'Hardcover'),
            ('SPEC', 'Spec'),
        ]

    name = models.CharField(max_length=255, verbose_name=_("Book title"))
    page_count = models.IntegerField(verbose_name=_("Page Count"))
    # category = models.CharField(max_length=255, verbose_name=_("Book category"))
    # author_name = models.CharField(max_length=255, verbose_name=_("Author Name"))
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=_("Price"))
    image = models.ImageField(upload_to='images/', verbose_name=_("Image"))
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    cover = models.CharField(max_length=9, choices=COVER_CHOICES, default='PAPERBACK')
    category = models.ManyToManyField(Category, default='undefined')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


