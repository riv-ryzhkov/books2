from django.shortcuts import render, redirect
from rest_framework import generics

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

def index(request):
    # books = [
    #     {
    #         "author": 'Pushkin',
    #         "id": '88',
    #         "title": 'Ruslan',
    #         "text": 'gjkhkjhlkj',
    #         "count": 8
    #     },
    #     {
    #         "author": 'Pushkin2',
    #         "id": '89',
    #         "title": 'Ruslan2',
    #         "text": 'gjkhkjhlkj222',
    #         "count": 10
    #     },
    # ]
    books = Book.objects.all()
    # books = Book.objects.order_by('-id')
    # books = Book.objects.order_by('-id')[:3]
    # books = Book.objects.filter(author='ГОСТ1')
    # books = Book.objects.filter(id__gt=2)
    # books = Book.objects.filter(id__lt=5)
    return render(request, 'main/index.html', {'title': 'Головна сторінка', 'books': books})
    # return render(request, 'main/index.html')


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
