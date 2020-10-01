from django.urls import path
from . import views

app_name = 'department'
urlpatterns = [
    path('', views.DepartmentMain.as_view(), name='index'),
    path('create/', views.DepartmentCreate.as_view(), name='create'),
    path('<int:pk>/update/', views.DepartmentUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.DepartmentDelete.as_view(), name='delete'),
]
