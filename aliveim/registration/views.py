from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import UserRegistrationForm


class UserRegistrationView(FormView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    success_url = '/thanks/'

    def form_valid(self, form):
        form.save()
        return super(UserRegistrationView, self).form_valid(form)


class UserRegistrationThanksView(TemplateView):
    template_name = 'thanks.html'
