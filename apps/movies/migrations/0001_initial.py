# Generated by Django 5.0.6 on 2024-06-12 21:53

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=500)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('resume', models.TextField(blank=True, null=True)),
                ('actors', models.ManyToManyField(related_name='movies', to='actors.actors')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='genres.genre')),
            ],
            options={
                'verbose_name': 'Filme',
                'verbose_name_plural': 'Filmes',
                'db_table': 'filmes',
                'ordering': ['-created_at'],
            },
        ),
    ]
