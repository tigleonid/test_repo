from django.urls import reverse_lazy
from django.views import generic
from .forms import StudentForm, LecturerForm


class StudentSignUpView(generic.CreateView):
    form_class = StudentForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class LecturerSignUpView(generic.CreateView):
    form_class = LecturerForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
