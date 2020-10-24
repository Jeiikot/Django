from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Employee
from .forms import EmployeeForm

class EmployeeMain(LoginRequiredMixin, View) :
    def get(self, request):
        count = Employee.objects.all().count()
        list_objects = Employee.objects.order_by('name')

        ctx = {'employee_count': count, 'employee_list': list_objects, 'title': 'Employees'}
        return render(request, 'employee/employee_list.html', ctx)


class EmployeeCreate(LoginRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee:index')


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee:index')


class EmployeeDelete(LoginRequiredMixin, DeleteView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee:index')