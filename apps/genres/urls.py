from django.urls import path
from .views import *


urlpatterns = [
    path('create-list/', GenreCreateListView.as_view(), name='genre_create_list'),
    path('update-delete/<str:pk>/', RetrieveUpdateDestroyView.as_view(), name='genre_update_delete'),
    path('genre-detail/<str:pk>/', GenreRetrieveView.as_view(), name='genre_genre_detail')
]
