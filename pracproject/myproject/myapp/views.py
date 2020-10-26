from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.contrib.auth.models import User
from .models import Person, NewUser, CustomerEntry
from .forms import PersonForm, UserSignupForm, CustomerEntryForm


# Create your views here.


# noinspection PyUnresolvedReferences
class HomePage(TemplateView):
    template_name = 'base.html'


# noinspection PyUnresolvedReferences
class PersonListView(ListView):
    model = Person
    template_name = 'about.html'

    def get_queryset(self):
        return Person.objects.all()


class PersonDetailView(LoginRequiredMixin, DetailView):
    # login_url = '/accounts/login/'
    model = Person
    template_name = 'detail.html'


class CreatePersonView(CreateView):
    template_name = 'add_person.html'
    model = Person
    form_class = PersonForm


class DeletePersonView(LoginRequiredMixin, DeleteView):
    # login_url = '/accounts/login/'
    model = Person
    success_url = reverse_lazy('person_list')


class UpdatePersonView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm

    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_staff:
    #         raise PermissionDenied
    #     return super().dispatch(request, *args, **kwargs)


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserSignupForm
    model = NewUser
    success_url = reverse_lazy('user_login')


class CustomerEntryView(CreateView):
    template_name = 'create_customer.html'
    form_class = CustomerEntryForm
    model = CustomerEntry
    success_url = reverse_lazy('customer_list')


class CustomerListView(ListView):
    context_object_name = "customer_objects"
    model = CustomerEntry
    template_name = 'customer_list.html'

    def get_queryset(self):
        return CustomerEntry.objects.all()


class UpdateCustomerView(UpdateView):
    model = CustomerEntry
    form_class = CustomerEntryForm
    success_url = reverse_lazy('customer_list')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CustomerInformation(DeleteView):
    model = CustomerEntry
    template_name = 'customer_info.html'
