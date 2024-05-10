'''
Страницы курсов и блоки для них
'''

from django.db import models
from unidecode import unidecode
from django.urls import reverse
from ..other.markdown import generate_html
from .profiles import Profile
from .user import LecturerUser


class Block(models.Model):
    # содержит в себе различные материалы, можно привязать к страницу

    # Page:
    # <Block>   <Block>
    # — Mat      — Mat
    # — Mat      — Mat
    # …
    OF_STUDENT = "student's"
    OF_LECTURER = "lecturer's"
    UNKNOWN = 'unknown'

    # генерируем html блока
    @property
    def html(self):
        return ''.join(['<div>' + str(m.concretize().view) + '</div>'
                         for m in self.materials.all()])
                         # просто берем каждый материал, конкретизируем и берем его
                         # view — т.е. html-код. Оборачиваем в div — и profit.

    # определение типа блока
    def type_(self):
        if self.pages_as_st.count():
            return Block.OF_STUDENT

        elif self.pages_as_lect.count():
            return Block.OF_LECTURER

        return Block.UNKNOWN

    # проверяем, может ли пользователь редактировать
    def can_edit(self, user):
        user = user.concretize()
        # каждый — только свою колонку
        return ((user.role == Profile.STUD_ROLE and self.type_ == Block.OF_STUDENT)
                or (user.role == Profile.LECT_ROLE and self.type_ == Block.OF_LECTURER))

    # краткое описание блока
    def __str__(self):
        return self.type_() + ' ' + ''.join(map(str, list(self.pages_as_st.all()) + list(self.pages_as_lect.all())))

    # страница, к которой привязан
    @property
    def related_page(self):
        if self.pages_as_st.count():
            return self.pages_as_st.get()
        else:
            return self.pages_as_lect.get()

# Страница курса
class CoursePage(models.Model):

    name = models.CharField('Название курса', max_length=50)
    slug = models.SlugField(max_length=255, verbose_name="URL")
    student_block = models.ForeignKey(Block, on_delete=models.CASCADE,
                                      related_name='pages_as_st')
    lecturer_block = models.ForeignKey(Block, on_delete=models.CASCADE,
                                       related_name='pages_as_lect')

    general_info = models.TextField('Общая информация')

    # можем указать основного преподавателя
    main_lecturer = models.ForeignKey(LecturerUser, null=True, on_delete=models.SET_NULL, related_name='pages_as_lect')

    # самописная функция для хорошей генерации slug-ов (имена страниц для ссылок)
    def create_slug(self):
        self.slug = unidecode(self.name).replace(' ', '_')
        copies = CoursePage.objects.all().filter(slug__startswith=self.slug)

        if copies: # если имя повторяется, дописываем номер в конец
            self.slug += str(len(copies) + 1)

    def __str__(self):
        return self.name

    @property
    def absolute_url(self):
        return reverse('pages', kwargs={'slug': self.slug})

# Страница чистого markdown
class MarkdownPage(models.Model):

    text = models.TextField()
    name = models.CharField('Название страницы', max_length=50)

    @property
    def html(self):
        return generate_html(self.text)

    def __str__(self):
        return self.name

    # у markdown-страниц нет slug-ов, только id
    @property
    def absolute_url(self):
        return reverse('view_markdown_page', kwargs={"id": self.id})
