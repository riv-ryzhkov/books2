from random import randint

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.forms import model_to_dict
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from rest_framework import generics, viewsets, mixins
from faker import Faker
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.viewsets import GenericViewSet

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Book
from .forms import BookForm
from .serializers import *


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookAPIjson(APIView):
    def get(self, request):
        filter = request.GET.get('id')
        b = Book.objects.all().filter(id__gt=filter)
        b = b.values()
        return Response({'title': 'GET работает!!!!', 'data': b})

    def post(self, request):
        post_new = Book.objects.create(
            title = request.data['title'],
            author = request.data['author'],
            text = request.data['text'],
            published = request.data['published'],
            count = request.data['count']
        )
        return Response({'post': model_to_dict(post_new)})




# class BookViewSet(viewsets.ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializerAuto




# class BookViewSet(
#             mixins.CreateModelMixin,   # создает
#             mixins.RetrieveModelMixin, # выделяет
#             mixins.UpdateModelMixin,   # обновляет
#             mixins.DestroyModelMixin,  # удаляет
#             mixins.ListModelMixin,     # показывает список
#             GenericViewSet             # главный родительский класс
# ):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializerAuto

class BookAPIPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class BookAPIList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerAuto
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = BookAPIPagination

class BookAPIUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerAuto
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


class BookAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializerAuto
    permission_classes = (IsAdminOrReadOnly, )



# class BookAPIAutoCreate(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializerAuto
#
#
# class BookAPIAutoUpdate(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializerAuto
#
#
# class BookAPIAutoCRUD(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializerAuto


class BookAPIser(APIView):
    def get(self, request):
        b = Book.objects.all()
        return Response({'posts': BookSerializer(b, many=True).data})

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # post_new = Book.objects.create(
        #     title = request.data['title'],
        #     author = request.data['author'],
        #     text = request.data['text'],
        #     published = request.data['published'],
        #     count = request.data['count']
        # )
        # return Response({'post': BookSerializer(post_new).data})
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Book.objects.get(id=id)
        except:
            return Response({'error': 'Object does not exists'})

        serializer = BookSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id', None)
        if not id:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Book.objects.get(id=id)
            instance.delete()
        except:
            return Response({'error': 'Method DELETE not allowed. Object does not exists'})

        return Response({'delete': 'post with id = ' + str(id) + ' deleted!'})



class BookHome(ListView):
    paginate_by = 10 #передает автоматически paginator и page_obj
    model = Book
    template_name = 'main/index.html'
    context_object_name = 'books'
    extra_context = {'title': 'Головна сторінка'}
    allow_empty = False

    def get_queryset(self):
        # last_id = Book.objects.first().id
        return Book.objects.filter(is_shown=True)

# def index(request):
#     books = Book.objects.all()
#     return render(request, 'main/index.html', {'title': 'Головна сторінка', 'books': books})

class IndexTab(ListView):
    paginate_by = 4
    model = Book
    template_name = 'main/index_tab.html'
    context_object_name = 'books'
    extra_context = {'numbers': 'із ' + str(len(Book.objects.all()))}
    allow_empty = False

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     books = Book.objects.filter(is_shown=True)
    #     books = books.order_by('-id')
    #     numbers = 'із ' + str(len(Book.objects.all()))
    #     return {'title': 'Книги', 'books': books, 'numbers': numbers}

    def get_queryset(self):
        return Book.objects.filter(is_shown=True)

# def index_tab(request):
#     books = Book.objects.order_by('-id')
#     numbers = 'із ' + str(len(Book.objects.all()))
#     return render(request, 'main/index_tab.html', {'title': 'Книги', 'books': books, 'numbers': numbers})


class BookView(DetailView):
    model = Book
    template_name = 'main/book_view.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book'
    allow_empty = False


# def book_view(request, id=1):
#     try:
#         book = Book.objects.get(id=id)
#     except Book.DoesNotExist:
#         raise Http404
#     return render(request, 'main/book_view.html', {'title': 'Книги', 'book': book})


class CreateBook(CreateView):
    paginate_by = 10
    form_class = BookForm
    template_name = 'main/create.html'
    success_url = reverse_lazy('home')



# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     form = BookForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'main/create.html', context)
#     # return render(request, 'main/create.html')


class BookEdit(LoginRequiredMixin, UpdateView):
    login_url = '/auth/login/?next=/tabs/'
    model = Book
    template_name = 'main/book_edit.html'
    fields = ['title', 'author', 'text', 'published', 'count']
    success_url = reverse_lazy('main')
    pk_url_kwarg = 'id'
    allow_empty = False

# def book_edit(request, id=0):
#     if request.method == "GET":
#         if id == 0:
#             form = BookForm()
#         else:
#             book = Book.objects.get(id=id)
#             form = BookForm(instance=book)
#         return render(request, 'main/book_edit.html', {'form': form})
#     else:
#         if id == 0:
#             form = BookForm(request.POST)
#         else:
#             book = Book.objects.get(id=id)
#             form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#         return redirect('main')


@login_required
def book_delete(request, id=0):
    try:
        book = Book.objects.get(id=id)
        book.delete()
    except Book.DoesNotExist:
        raise Http404
    books = Book.objects.order_by('-id')
    numbers = 'із ' + str(len(Book.objects.all()))
    return render(request, 'main/index_tab.html', {'title': 'Книги', 'books': books, 'numbers': numbers})






def about(request):

    context_list = Book.objects.all()
    paginator = Paginator(context_list, 3)

    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'main/about.html', {'title': 'About site', 'books_page': page_obj})


def book_new(request):
    b = Faker()
    b_new = Book.objects.create(
        title=b.company(),
        author=b.last_name(),
        text=' '.join(b.sentences(20)),
        published = str(b.year()),
        is_shown = True,
        count = randint(1, 20)
    )
    b_new.save()
    # Book.save()
    # books = list(Book.objects.all())
    books = Book.objects.order_by('-id')[:10]
    numbers = '10 нових із ' + str(len(Book.objects.all()))
    return render(request, 'main/book_view.html', {'title': 'Книги', 'book': b_new, 'books': books, 'numbers': numbers})

