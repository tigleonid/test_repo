'''
Формы для создания материалов для курсов
'''

from embed_video.fields import EmbedVideoFormField

from ..models import File, Url, Video, MarkdownMat, MaterialContainer, IFrame, CoursePage, Block
from ..models import LecturerUser
from django.forms import ModelForm, TextInput, Textarea, FileField
from django import forms


# Форма для ввода чистого маркдауна
class MarkdownMatForm(ModelForm):
    class Meta:
        model = MarkdownMat
        fields = ('text',)



# Форма для создания новых контейнеров

# Увы, далеко не идеальная реализация — быстрая, "на коленке".
# Сейчас оно позволяет прикрепить по одному элементу каждого типа
# В идеале нужно сделать так, чтобы для каждого элемента *можно* было
# добавить сколько нужно полей. Проще всего это сделать через кучу мелких форм,
# которые появляются после нажатия соотвествующих кнопок 
class ContainerForm(forms.Form):
    markdown_text = forms.CharField(required=False, widget=Textarea)
    url_material = forms.URLField(required=False)
    video_material = EmbedVideoFormField(required=False)
    file_material = FileField(required=False)
    frame_url = forms.URLField(required=False)

    def clean(self):
        form_data = self.cleaned_data
        if not any(form_data):
            self.add_error("Добавьте текст/материалы")
        return form_data

    def save(self, parent=None):

        # отвратительный код, буду рад, если кто напишет получше

        # выбираем "чистые" данные из введенных
        m_text, u_m, v_m, file_m, frame_m = (self.cleaned_data["markdown_text"], self.cleaned_data["url_material"],
                                             self.cleaned_data["video_material"], self.cleaned_data["file_material"],
                                             self.cleaned_data["frame_url"])
        # создаем заготовки
        t = MarkdownMat()
        t.text = m_text
        t.save()

        c = MaterialContainer(markdown=t)
        c.save()

        # и дальше проходимся по всем данным,
        if u_m:
            # если не пустые — создаем соответствующие элементы
            u = Url()
            u.address = u_m
            u.text = u_m
            u.save()
            c.urls.add(u)

        if v_m:
            v = Video()
            v.video_material = v_m
            v.save()
            c.videos.add(v)

        if file_m:
            f = File()
            f.file_material = file_m
            f.name = file_m.name
            f.save()
            c.files.add(f)

        if frame_m:
            frame = IFrame()
            frame.frame_url = frame_m
            frame.save()
            c.frames.add(frame)

        # привязываем заготовку с элементами к указанному элементу
        c.parent = parent
        c.save()

        return c


# Создание нового курса
class CreateCourseForm(ModelForm):
    class Meta:
        model = CoursePage
        fields = ["name", "general_info"]
        widgets = {"name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название курса'
        }),
            'general_info': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Общая информация'
            }),
        }

    def save(self, commit=True):
        page = super(ModelForm, self).save(commit=False)

        # создаем колонки для студентов и преподователей
        page.lecturer_block = Block()
        page.lecturer_block.save()

        page.student_block = Block()
        page.student_block.save()
        if commit:
            page.save()
        return page


class EditCourseGeneralInfo(ModelForm):
    main_lecturer = forms.ModelChoiceField(queryset=LecturerUser.objects.all(), required=False)
    class Meta:
        model = CoursePage
        fields = ['general_info', 'main_lecturer']
