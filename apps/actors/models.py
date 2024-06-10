from django.db import models

from apps.core.models import BaseModel

from .nationalites import NATIONALITIES


class Actors(BaseModel):
    name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=3, choices=NATIONALITIES,
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ator'
        verbose_name_plural = 'Atores'
        ordering = ['-created_at']
        db_table = 'atores'
