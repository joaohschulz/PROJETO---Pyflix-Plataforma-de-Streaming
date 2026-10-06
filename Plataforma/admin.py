from django.contrib import admin
from .models import Filmes, Episodios, Series

class FilmesAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao', 'categoria', 'cartaz']
class EpisodiosAdmin(admin.ModelAdmin):
    list_display = ['nome_da_serie', 'episodio', 'temporada', 'categoria']
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['nome_da_serie',]
    
admin.site.register(Filmes, FilmesAdmin)
admin.site.register(Episodios, EpisodiosAdmin)
admin.site.register(Series, SeriesAdmin)