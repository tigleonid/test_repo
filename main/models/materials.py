"""
Модуль с модельками всех возможных материалов
"""

from django.db import models
from embed_video.fields import EmbedVideoField

from model_utils.managers import InheritanceManager
from django.template import Template, Context
from ..other.markdown import generate_html


# материалы бывают разными, и нам хочется уметь получать точный тип
class MaterialMaster(InheritanceManager):
    pass


# "интерфейс" для остальных материалов
class Material(models.Model):
    objects = MaterialMaster() # менеджер материалов для конкретизации

    # блок, к которому прикреплен материал
    parent = models.ForeignKey('Block', on_delete=models.CASCADE, null=True, related_name='materials')

    # master = models.ForeignKey(MaterialMaster)


    # html-код, генерируемый материалом для отображения
    @property
    def view(self):
        pass

    # аналогично пользователям (см. user.py) — 
    # возвращает уточненную версию с её параметрами
    def concretize(self):
        "return inherited version of self"
        return Material.objects.get_subclass(id=self.id)

    # отображение в админке
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы' # как отображается группа в адмике
        ordering = ['-id'] # для удобства отсортуируем по id 
        # (т.е. де-факто по дате создания)


# отображение ссылок
class Url(Material):
    address = models.URLField(max_length=200) # непосредственно адрес, куда переходим
    text = models.TextField() # внешний текст ссылки, что видит пользователь

    @property
    def view(self):
        return f'<a href="{self.address}">{self.text}</a>'


# прикрепленный пользователем файл
class File(Material):
    file_material = models.FileField(null=True, upload_to='documents') # сам файл
    uploaded_at = models.DateTimeField(auto_now_add=True) # когда загрузили
    name = models.CharField(max_length=30) # отображаемое название-ссылка

    @property
    def view(self):
        return f'<a href="{self.file_material.url}" download>{self.name}</a>'


# видео (например, с YouTube)
class Video(Material):
    video_material = EmbedVideoField()
    name = models.CharField(max_length=30) # в данный момент не используется, можно убрать,
    # а можно дописать во view name, если покажется полезным

    def __str__(self):
        return str(self.video_material)

    @property
    def view(self):
        return Template(f'''{{% load embed_video_tags %}}
        {{% video material '600x400' %}}''').render(Context({'material': self.video_material}))


# текст в разметке markdown
class MarkdownMat(Material):
    text = models.TextField(blank=True)

    @property
    def view(self):
        # generate_html — метод из other.markdown
        # для генерации html из md
        return generate_html(self.text)

# вставка куска чужого сайта (например, расписание из Google Таблиц)
class IFrame(Material):
    frame_url = models.URLField(max_length=200)

    @property
    def view(self):
        return f'<iframe src="{self.frame_url}" style="height: 500px;width: 80%;allow=fullscreen;border:none"></iframe>'


# обычно мы хотим прикреплять не один элемент, а сразу несколько, "объединяя" их
# эта штука хранит в себе все возможные комбинируемые элементы
class MaterialContainer(Material):
    markdown = models.ForeignKey(MarkdownMat, on_delete=models.CASCADE)
    urls = models.ManyToManyField(Url)
    videos = models.ManyToManyField(Video)
    files = models.ManyToManyField(File)
    frames = models.ManyToManyField(IFrame)

    @property
    def view(self):
        return ('<div class="material-container">'

                + Template(f'''<a class="close-mat" href="{{% url 'remove_material' slug id %}}">×</a>''').render(Context({'id': self.id,
                                                                                                         'slug': self.parent.related_page.slug}))

                + ''.join(['<div>' + str(m.concretize().view) + '</div>'
                                          for m in [self.markdown]
                                          + list(self.urls.all())
                                          + list(self.videos.all())
                                          + list(self.files.all())
                                          + list(self.frames.all())])
                
                + '</div>')
