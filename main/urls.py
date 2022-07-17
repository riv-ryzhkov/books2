from django.urls import path, include, re_path
from . import views
from .views import *

# from rest_framework import routers
#
#
# router = routers.SimpleRouter()
# router.register(r'detail', BookViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('tabs', views.index_tab, name='main'),
    path('create', views.create, name='create'),
    path('book/<int:id>/view', views.book_view, name='book_view'),
    path('book/<int:id>/edit', views.book_edit, name='book_edit'),
    path('book/<int:id>/delete', views.book_delete, name='book_delete'),
    path('book/new', views.book_new, name='book_new'),
    path('api/v1/', BookAPIView.as_view(), name='APIbooklist'),
    path('api/v2/', BookAPIjson.as_view(), name='APIbookjsonv2'),

    # # path('api/v3/', BookAPIser.as_view(), name='APIbookPOST'),
    # path('api/v3/', BookAPIAutoCreate.as_view(), name='APIbookPOST'),
    #
    # # path('api/v3/<int:id>/', BookAPIser.as_view(), name='APIbookPUT'),
    # path('api/v3/<int:pk>/', BookAPIAutoUpdate.as_view(), name='APIbookPUT'),
    #
    # path('api/v3/detail/<int:pk>/', BookAPIAutoCRUD.as_view(), name='APIbookCRUD'),
    # path('api/v3/', BookViewSet.as_view(), name='APIViewSet'),

    # path('api/v4/', include(router.urls)),   # http://127.0.0.1:8000/api/v4/detail/
    # path('api/v3/detail/<int:pk>/', BookAPIAutoCRUD.as_view(), name='APIbookCRUD'),
    path('api/v3/book/', BookAPIList.as_view()),
    path('api/v3/book/<int:pk>/', BookAPIUpdate.as_view()),
    path('api/v3/bookdelete/<int:pk>/', BookAPIDestroy.as_view()),

    path('api/v3/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]