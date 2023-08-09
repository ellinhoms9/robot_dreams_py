from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from users.models import Users


class UsersListView(ListView):
    model = Users
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UsersDetailView(DetailView):
    model = Users
    template_name = 'users/users_detail.html'
    context_object_name = 'users'


class UsersCreateView(CreateView):
    model = Users
    template_name = 'users/users_create.html'
    context_object_name = 'users/users_create.html'
    fields = ('first_name', 'last_name', 'age', 'username')
    success_url = reverse_lazy('users:users-list')
