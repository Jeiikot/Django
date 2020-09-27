from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.template import loader

from .models import FilmGenres, Film

def index(request):
    latest_filmGenres_list = FilmGenres.objects.all()
    context = {
        'latest_filmGenres_list': latest_filmGenres_list
    }
    return render(request, 'movie_polls/index.html', context)

def detail(request, filmGenres_id):
    filmGenres = get_object_or_404(FilmGenres, pk=filmGenres_id)
    context = {
        'filmGenres': filmGenres
    }
    return render(request, 'movie_polls/detail.html', context)

def results(request, filmGenres_id):
    filmGenres = get_object_or_404(FilmGenres, pk=filmGenres_id)
    context = {
        'filmGenres': filmGenres
    }
    return render(request, 'movie_polls/results.html', context)

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