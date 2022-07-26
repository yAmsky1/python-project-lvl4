from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .translations import (
    LOGGED_IN_MESSAGE,
    LOGGED_OUT_MESSAGE,
    LOGIN_BUTTON,
    LOGIN_TITLE
)


class Index(TemplateView):
    template_name = "index.html"


class Login(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    success_message = LOGGED_IN_MESSAGE
    next_page = reverse_lazy('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = LOGIN_TITLE
        context['button_text'] = LOGIN_BUTTON
        return context


class Logout(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, LOGGED_OUT_MESSAGE)
        return super().dispatch(request, *args, **kwargs)
