from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField('Назва', max_length=50, default='The title of the book')
    author = models.CharField('Автор', max_length=50, default='Unknown author')
    text = models.TextField('Опис', default='Text about the book')
    published = models.CharField('Рік видання', max_length=4, default='2022')
    count = models.IntegerField('Кількість', default=1)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
