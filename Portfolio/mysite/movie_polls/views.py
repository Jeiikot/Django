from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
# from django.template import loader

from .models import FilmGenres, Film

class IndexView(generic.ListView):
    template_name = 'movie_polls/index.html'
    context_object_name = 'latest_filmGenres_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return FilmGenres.objects.all()


class DetailView(generic.DetailView):
    model = FilmGenres
    template_name = 'movie_polls/detail.html'
    context_object_name = 'filmGenres'

class ResultsView(generic.DetailView):
    model = FilmGenres
    template_name = 'movie_polls/results.html'
    context_object_name = 'filmGenres'


def vote(request, filmGenres_id):
    filmGenres = get_object_or_404(FilmGenres, pk=filmGenres_id)
    try:
        selected_film = filmGenres.film_set.get(pk=request.POST['film'])
    except (KeyError, Film.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'movie_polls/detail.html', {
            'filmGenres': filmGenres,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_film.votes += 1
        selected_film.save()
        return HttpResponseRedirect(reverse('movie_polls:results', args=(filmGenres.id,)))