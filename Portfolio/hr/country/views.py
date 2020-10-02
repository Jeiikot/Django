from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Country
from .forms import CountryForm

class CountryMain(LoginRequiredMixin, View) :
    def get(self, request):
        count = Country.objects.all().count()
        list_objects = Country.objects.order_by('name')

        ctx = {'country_count': count, 'country_list': list_objects}
        return render(request, 'country/country_list.html', ctx)


class CountryCreate(LoginRequiredMixin, CreateView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('country:index')


class CountryUpdate(LoginRequiredMixin, UpdateView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('country:index')


class CountryDelete(LoginRequiredMixin, DeleteView):
    model = Country
    fields = '__all__'
    success_url = reverse_lazy('country:index')