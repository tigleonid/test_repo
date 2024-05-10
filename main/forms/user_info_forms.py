'''
Формы, которые будут отображаться в профиле для изменения личной информации.
'''

from ..models import Profile
from django import forms


class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo", "first_name", "last_name", "patronymic"]


class EditStudentForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = EditUserForm.Meta.fields + ["course", "program_level", "course_number"]


class EditLecturerForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = EditUserForm.Meta.fields + ["link", "story"]
