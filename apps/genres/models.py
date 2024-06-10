from django.db import models

from apps.core.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['-created_at']
        db_table = 'genero'
