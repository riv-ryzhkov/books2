from django.urls import path
from . import views
from .views import BookAPIView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('api/v1/booklist/', BookAPIView.as_view(), name='APIbooklist')
]