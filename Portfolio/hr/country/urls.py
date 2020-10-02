from django.urls import path
from . import views

app_name = 'country'
urlpatterns = [
    path('', views.CountryMain.as_view(), name='index'),
    path('create/', views.CountryCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.CountryUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.CountryDelete.as_view(), name='delete'),
]
