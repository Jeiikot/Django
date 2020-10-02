from django.urls import path
from . import views

app_name = 'job'
urlpatterns = [
    path('', views.JobMain.as_view(), name='index'),
    path('create/', views.JobCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.JobUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.JobDelete.as_view(), name='delete'),
]
