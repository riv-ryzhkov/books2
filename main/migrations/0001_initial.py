# Generated by Django 4.0.4 on 2022-07-30 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='The title of the book', max_length=50, verbose_name='Назва')),
                ('author', models.CharField(default='Unknown author', max_length=50, verbose_name='Автор')),
                ('text', models.TextField(default='Text about the book', verbose_name='Опис')),
                ('published', models.CharField(default='2022', max_length=4, verbose_name='Рік видання')),
                ('is_shown', models.BooleanField(default=True, verbose_name='Показувати')),
                ('count', models.IntegerField(default=1, verbose_name='Кількість')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['-created', 'title'],
            },
        ),
    ]
