from django.urls import path

from . import views

app_name = 'movie_polls'
urlpatterns = [
    path('', views.index, name='index'),

    path('<int:filmGenres_id>/', views.detail, name='detail'),
    path('<int:filmGenres_id>/results/', views.results, name='results'),
    path('<int:filmGenres_id>/vote/', views.vote, name='vote'),
]