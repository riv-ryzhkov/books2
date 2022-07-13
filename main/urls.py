from django.urls import path
from . import views
from .views import BookAPIView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tabs', views.index_tab, name='main'),
    path('create', views.create, name='create'),
    path('book/<int:id>/view', views.book_view, name='book_view'),
    path('book/<int:id>/edit', views.book_edit, name='book_edit'),
    path('book/<int:id>/delete', views.book_delete, name='book_delete'),
    path('book/new', views.book_new, name='book_new'),
    path('api/v1/booklist/', BookAPIView.as_view(), name='APIbooklist')
]