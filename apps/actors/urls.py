from django.urls import path
from .views import *


urlpatterns = [
    path('create-list/', ActorCreateListView.as_view(), name='actor_create_list'),
    path('update-delete/<str:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor_update_delete'),
    path('actor-detail/<str:pk>/', ActorRetrieveView.as_view(), name='actor_genre_detail')
]
