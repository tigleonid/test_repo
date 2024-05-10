"""
Forms used for registering new users 
"""

from main.models import EmailUser, StudentUser, LecturerUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class BasicRegistrationForm(UserCreationForm):
    required_css_class = 'required'

    # this string is important because it allows to edit username
    first_name = forms.CharField(label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия',
                                widget=forms.TextInput(attrs={'class': 'form-input'}))

    patronymic = forms.CharField(label='Отчество',
                                 widget=forms.TextInput(attrs={'class': 'form-input'}), required=False)

    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    password2 = forms.CharField(label='Повтор пароля',
                                widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-input'}), required=True)

    class Meta:
        model = EmailUser
        fields = ('first_name', 'last_name', 'patronymic',
                  'email', 'password1', 'password2')
        abstract = True

    def save(self, user_type, commit=True):
        first_name = self.cleaned_data["first_name"]
        second_name = self.cleaned_data["last_name"]

        user = user_type.objects.create_user(email=self.cleaned_data["email"],
                                             password=self.cleaned_data["password1"])

        user.profile.first_name = first_name
        user.profile.last_name = second_name  # DEBUG!!!
        user.profile.patronymic = self.cleaned_data["patronymic"]

        if commit:
            user.save()
            user.profile.save()

        return user


class StudentForm(BasicRegistrationForm):

    course = forms.ChoiceField(label='Направление', choices=[('Физика', 'Физика'),
                                                             ('ПМИ', 'ПМИ')],
                               initial=('Физика', 'Физика'))

    program_level = forms.ChoiceField(label='Программа', choices=[('Бакалавриат', 'Бакалавриат'),
                                                                  ('Магистратура', 'Магистратура')],
                                      initial=('Бакалавриат', 'Бакалавриат'))

    course_number = forms.ChoiceField(label='Курс', choices=[(i, i) for i in range(1, 4 + 1)],
                                      initial=(1))

    class Meta:
        model = EmailUser
        fields = BasicRegistrationForm.Meta.fields + ('course', 'program_level', 'course_number')

    def save(self, commit=True):
        user = super().save(StudentUser, commit=False)
        user.profile.course = self.cleaned_data["course"]
        user.profile.program_level = self.cleaned_data["program_level"]
        user.profile.course_number = self.cleaned_data["course_number"]

        if commit:
            user.save()
            user.profile.save()
        return user


class LecturerForm(BasicRegistrationForm):
    link = forms.URLField(label='Связь с Вами:', required=False)

    class Meta:
        model = EmailUser
        fields = BasicRegistrationForm.Meta.fields + ('link',)

    def save(self, commit=True):
        user = super().save(LecturerUser, commit=False)
        user.profile.link = self.cleaned_data["link"]

        if commit:
            user.save()
            user.profile.save()

        return user
