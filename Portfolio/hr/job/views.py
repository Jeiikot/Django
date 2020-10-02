from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Job
from .forms import JobForm

class JobMain(LoginRequiredMixin, View) :
    def get(self, request):
        count = Job.objects.all().count()
        list_objects = Job.objects.order_by('name')

        ctx = {'job_count': count, 'job_list': list_objects}
        return render(request, 'job/job_list.html', ctx)


class JobCreate(LoginRequiredMixin, CreateView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('job:index')


class JobUpdate(LoginRequiredMixin, UpdateView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('job:index')


class JobDelete(LoginRequiredMixin, DeleteView):
    model = Job
    fields = '__all__'
    success_url = reverse_lazy('job:index')