from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField('Назва', max_length=50, default='The title of the book')
    author = models.CharField('Автор', max_length=50, default='Unknown author')
    text = models.TextField('Опис', default='Text about the book')
    published = models.CharField('Рік видання', max_length=4, default='2022')
    is_shown = models.BooleanField(default=True, verbose_name='Показувати')
    count = models.IntegerField('Кількість', default=1)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.PROTECT, default=1, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post', kwargs={'id': self.pk})
        return reverse('book_view', kwargs={'id': self.pk})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-created', 'title'] # сотрировка действует везде по умолчанию
