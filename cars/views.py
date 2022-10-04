from re import template
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from .forms import RegisterUserForm, LoginUserForm, CommentForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login

from .utils import DataMixin

from .models import Car, Comment, TechSpec


class HomeView(DataMixin, TemplateView):
    template_name = 'cars/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Home")
        return dict(list(context.items()) + list(c_def.items()))


class CarsView(DataMixin, ListView):
    template_name = 'cars/cars.html'
    context_object_name = 'cars_list'

    def get_queryset(self):
        return Car.objects.get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Cars catalog")
        return dict(list(context.items()) + list(c_def.items()))


class DetailView(DataMixin, DetailView, CreateView):

    form_class = CommentForm
    success_url = reverse_lazy('home')

    model = Car
    template_name = 'cars/detail.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user_id = self.request.user.id
        car = Car.objects.get(pk=self.kwargs['pk'])
        comment.car_id = car.id
        comment.save()
        return redirect('detail', self.kwargs['pk'])

    def get_queryset(self):
        return Car.objects.get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Specifications")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):

    form_class = RegisterUserForm
    template_name = 'cars/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign up")
        return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):

    form_class = LoginUserForm
    template_name = "cars/login.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Sign in")
        return dict(list(context.items()) + list(c_def.items()))


def logout_user(request):

    logout(request)
    return redirect('home')
