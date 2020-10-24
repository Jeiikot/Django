from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Department
from .forms import DepartmentForm

class DepartmentMain(LoginRequiredMixin, View) :
    def get(self, request):
        count = Department.objects.all().count()
        list_objects = Department.objects.order_by('name')

        ctx = {'department_count': count, 'department_list': list_objects, 'title': 'Deparments'}
        return render(request, 'department/department_list.html', ctx)


class DepartmentCreate(LoginRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('department:index')


class DepartmentUpdate(LoginRequiredMixin, UpdateView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('department:index')


class DepartmentDelete(LoginRequiredMixin, DeleteView):
    model = Department
    fields = '__all__'
    success_url = reverse_lazy('department:index')