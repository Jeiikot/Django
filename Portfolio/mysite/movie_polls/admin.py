from django.contrib import admin

from .models import FilmGenres, Film

admin.site.register(FilmGenres)
admin.site.register(Film)