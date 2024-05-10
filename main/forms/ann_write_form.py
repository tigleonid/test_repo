# Формы для создания объявлений и "чистых" markdown-страниц

from ..models import Announcement, Profile, MarkdownPage

from django import forms


# базовое отправление объявления
# (нужно будет напихать больше параметров — например,
# отправить конкретной группе людей)

class WriteAnnounceForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ["name", "text"]
        # exclude = ["sender", "receivers"]  # user must't be able to edit these


# преподаватель может выбрать, какому курсу отправить объявление
class WriteLectorsForm(WriteAnnounceForm):
    course_number = forms.ChoiceField(label='Курс', choices=[(i, i) for i in range(1, 4 + 1)],
                                      initial=(1))


# создание чистой markdown-страницы
class CreateMarkdownPageForm(forms.ModelForm):
    class Meta:
        model = MarkdownPage
        exclude = []
