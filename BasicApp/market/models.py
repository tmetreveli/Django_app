from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Book title"))
    page_count = models.IntegerField(verbose_name=_("Page Count"))
    category = models.CharField(max_length=255, verbose_name=_("Book category"))
    author_name = models.CharField(max_length=255, verbose_name=_("Author Name"))
    price = models.DecimalField(decimal_places=3, max_digits=5, verbose_name=_("Price"))
    image = models.ImageField(upload_to='images/', verbose_name=_("Image"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
