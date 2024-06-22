from django.db import models
from django.core.validators import MaxValueValidator, MinValidationValue

class Profile(models.Model):
    NO_ROLE = ''
    LECT_ROLE = 'Преподаватель'
    STUD_ROLE = 'Студент'

    roles_repr = {NO_ROLE: 'Аноним', LECT_ROLE: LECT_ROLE, STUD_ROLE: STUD_ROLE}

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True)  # Middle name
    photo = models.ImageField(upload_to='profiles', blank=True)

    # Student fields
    course = models.CharField(max_length=30, blank=True)
    program_level = models.CharField(max_length=30, blank=True)
    course_number = models.IntegerField(null=True, blank=True)
    grades = models.JSONField(default=dict)  # Storing grades as a JSON field
    status = models.CharField(max_length=20, choices=(('active', 'Active'), ('interrupted', 'Interrupted')),
                              default='active')

    # Lecturer fields
    link = models.URLField(max_length=200, blank=True)
    story = models.TextField(blank=True)

    # Property for convenience
    @property
    def role(self):
        return self.user.role

    def get_full_name(self):
        return ' '.join([self.first_name, last_name, self.patronymic])

    def __str__(self):
        child = self.user.concretize()
        return ((self.roles_repr[child.role] if child.role in self.roles_repr
                 else 'unknown') + ' ' + self.get_full_name())