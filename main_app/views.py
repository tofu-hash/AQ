from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class ProfileView(TemplateView):
    template_name = 'profile/index.html'


class CreateQuestionView(TemplateView):
    template_name = 'questions/create.html'


class HomeView(TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'auth/login.html'


class RegisterView(TemplateView):
    template_name = 'auth/register.html'
