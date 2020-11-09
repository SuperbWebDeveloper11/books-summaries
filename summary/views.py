from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
# messages framework
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
# class-based generic views
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# import models
from django.contrib.auth.models import User
from .models import Summary


class SummaryList(ListView): 
    model = Summary
    template_name = 'summary/summary/summary_list.html'
    context_object_name = 'summary_list'
    paginate_by = 5


class SummaryDetail(DetailView):
    model = Summary
    template_name = 'summary/summary/summary_detail.html'
    context_object_name = 'summary'


class SummaryCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView): 
    model = Summary
    template_name = 'summary/summary/summary_form_create.html' 
    fields = ['title', 'body']
    success_message = "Summary was created successfully"

    def form_valid(self, form):
        form.instance.owner = self.request.user # add summary owner 
        return super().form_valid(form)


class SummaryUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Summary
    template_name = 'summary/summary/summary_form_update.html' 
    fields = ['title', 'body']
    success_message = "Summary was updated successfully"

    def form_valid(self, form):
        # user should be the summary owner 
        if form.instance.owner == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('You are not summary owner')


class SummaryDelete(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Summary
    template_name = 'summary/summary/summary_confirm_delete.html' 
    success_message = "Summary was deleted successfully"
    success_url = reverse_lazy('summary:summary_list')

    def form_valid(self, form):
        # user should be the summary owner 
        if form.instance.publisher == self.request.user:
            return super().form_valid(form)
        else:
            return HttpResponse('You are not summary owner')

    def delete(self, request, *args, **kwargs):
        # inform user that "Summary was deleted successfully"
        messages.info(request, self.success_message)
        return super().delete(request, *args, **kwargs)

