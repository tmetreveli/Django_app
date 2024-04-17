# Generated by Django 5.0.3 on 2024-04-17 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_remove_book_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Author name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='market.author', verbose_name='Book Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(default='undefined', to='market.category', verbose_name='Book Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.CharField(choices=[('PAPERBACK', 'Paperback'), ('HARDCOVER', 'Hardcover'), ('SPEC', 'Spec')], default='PAPERBACK', max_length=9, verbose_name='Book cover'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('FANTASY', 'fantasy'), ('ROMANCE', 'romance'), ('DOCUMENTARY', 'documentary'), ('UNDEFINED', 'undefined')], default='PAPERBACK', max_length=11, verbose_name='Category name'),
        ),
    ]
