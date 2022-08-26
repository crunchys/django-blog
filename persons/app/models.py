from django.db import models
from django.urls import reverse


class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)
    bio = models.TextField(blank=True, verbose_name='Биография')
    years_live = models.CharField(max_length=50, verbose_name='Годы жизни')
    photo = models.ImageField(blank=True, upload_to='uploads/')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Великие люди'
        verbose_name_plural = 'Великие люди'
        ordering = ['-id']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, verbose_name='URL', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
