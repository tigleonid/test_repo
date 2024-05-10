"""
Модель для хранения объявленияs
"""

from django.db import models
from . import EmailUser
from ..other.markdown import generate_html


class Announcement(models.Model):
    # автор объявления
    sender = models.ForeignKey(EmailUser, on_delete=models.CASCADE, related_name='sent_announcements')
    
    # кто его может видеть
    receivers = models.ManyToManyField(EmailUser, related_name='recieved_announcements')
    # с этим связана одна не слишком приятная особенность — объявление видят только
    # пользователи, которые УЖЕ БЫЛИ зарегистрированы на момент его отправки
    # это неплохо — нет устаревшего спама
    # …но если захочется исправить — нужно начинать с изменения того, как хранятся получатели
    # например, можно хранить параметры вроде "группы"/"отдельного пользователя" и тп. 
   
    # заголовок объявления — на самом деле просто "# name" в первой строчке
    name = models.CharField(max_length=30)
    
    # собственно, markdown-текст
    text = models.TextField()

    @property
    def html(self):
        return generate_html('# ' + self.name + '\n' + self.text)

    class Meta:
        ordering = ['-id'] # сортируем для удобства по id, т.е. по дате создания
