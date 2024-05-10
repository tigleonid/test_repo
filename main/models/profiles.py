"""
Каждый пользователь имеет профиль, в котором хранятся все его возможные данные
(и невозможные тоже — преподаватели хранят пустое поле для номера курса и тп)
Это была временная мера, сейчас эту информацию можно переместить в пользователей,
но не уверен, нужно ли.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    NO_ROLE = ''
    LECT_ROLE = 'Преподаватель'
    STUD_ROLE = 'Студент'

    roles_repr = {NO_ROLE: 'Аноним ', LECT_ROLE: LECT_ROLE,
                  STUD_ROLE: STUD_ROLE}

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # это отчество, если что
    patronymic = models.CharField(max_length=30, blank=True)

    photo = models.ImageField(upload_to='profiles', blank=True)

    # для удобства — можем писать profile.role, не дублируя информацию
    @property
    def role(self):
        "Important: doesn't concretize user"
        return self.user.role

    # for students

    course = models.CharField(max_length=30, blank=True)
    program_level = models.CharField(max_length=30, blank=True)
    course_number = models.IntegerField(null=True, blank=True)

    # for lectors

    link = models.URLField(max_length=200, blank=True)
    story = models.TextField(blank=True)

    # college = models.CharField(max_length=30, default = 'HSE')
    # major = models.CharField(max_length=30, default = 'Physics')

    # генерируем ФИО
    def get_full_name(self):
        return ' '.join([self.first_name,
                         self.last_name,
                         self.patronymic, ])

    # ФИО + "должность"
    def __str__(self):
        child = self.user.concretize()
        return ((self.roles_repr[child.role] if child.role in self.roles_repr
                 else 'unknown') + ' ' + self.get_full_name())
