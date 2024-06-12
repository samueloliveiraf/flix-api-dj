from django.db import models

from apps.core.models import BaseModel
from apps.actors.models import Actors
from apps.genres.models import Genre


class Movie(BaseModel):
    title = models.CharField(
        max_length=500
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        related_name='movies'
    )
    release_date = models.DateField(
        null=True, blank=True
    )
    actors = models.ManyToManyField(
        Actors,
        related_name='movies'
    )
    resume = models.TextField(
        null=True, blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['-created_at']
        db_table = 'filmes'
