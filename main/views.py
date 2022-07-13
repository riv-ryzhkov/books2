from random import randint

from django.shortcuts import render, redirect
from rest_framework import generics
from faker import Faker

from .models import Book
from .forms import BookForm
from .serializers import BookSerializers


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers






def index(request):

    books = Book.objects.all()
    # books = Book.objects.order_by('-id')
    # books = Book.objects.order_by('-id')[:3]
    # books = Book.objects.filter(author='ГОСТ1')
    # books = Book.objects.filter(id__gt=2)
    # books = Book.objects.filter(id__lt=5)
    return render(request, 'main/index.html', {'title': 'Головна сторінка', 'books': books})
    # return render(request, 'main/index.html')

def index_tab(request):
    # books = Book.objects.all()
    # books = Book.objects.order_by('-id')[:10]
    books = Book.objects.order_by('-id')
    numbers = 'із ' + str(len(Book.objects.all()))
    return render(request, 'main/index_tab.html', {'title': 'Книги', 'books': books, 'numbers': numbers})




def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = BookForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)
    # return render(request, 'main/create.html')

# Create your views here.

def book_new(request):
    b = Faker()
    b_new = Book.objects.create(
        title=b.company(),
        author=b.last_name(),
        text=' '.join(b.sentences(3)),
        published = str(b.year()),
        count = randint(1, 20)
    )
    b_new.save()
    # Book.save()
    # books = list(Book.objects.all())
    books = Book.objects.order_by('-id')[:10]
    numbers = '10 нових із ' + str(len(Book.objects.all()))
    return render(request, 'main/index_tab.html', {'title': 'Книги', 'books': books, 'numbers': numbers})

