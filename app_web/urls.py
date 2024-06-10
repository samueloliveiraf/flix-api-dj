from django.contrib import admin
from django.urls import path, include

from apps.accounts import urls as urls_account
from apps.genres import urls as urls_genres
from apps.actors import urls as urls_actors


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(urls_account)),
    path('genres/', include(urls_genres)),
    path('actors/', include(urls_actors)),
]
