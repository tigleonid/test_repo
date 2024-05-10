"""
Функции отображения для объявлений
"""

from .. import models

from django.shortcuts import render, redirect
from ..models import Announcement, EmailUser
from django.core.exceptions import PermissionDenied
from ..forms import WriteAnnounceForm, WriteLectorsForm
from django.contrib.auth.decorators import login_required


# на самом деле это костыль:
# из-за того, что мы не хотим использовать ajax (для JS)
# нам нужно каждый запрос проверять на то,
# что в нём не нажимается кнопка закрытия объявления
# эта функция этой проверкой и занимается
#
# ВАЖНО: эту функцию нужно вызывать во всех вызовах отображений
# где есть выпадающие объявления, иначе они не будут работать
#
# P.S. сюда же можно подключить обработку других подобных событий,
# которыми нужно управлять со всех страниц
def header_handler(request):
    "makes 'close' buttons on header announcements work"
    if request.method != "POST":
        return # если не POST запрос, то кнопка точно не нажимается

    keys = request.POST.keys()

    # ищем среди ключей POST-запроса нажатие кнопки удаления объявления
    keys = list(filter(lambda t: t.startswith('delete_announcement_'), keys))


    if not len(keys):
        return # не нашли, уходим
    
    key = keys[0] # если нашли => есть ключ, отвечающий за закрытие объявления
    id = int(key[len('delete_announcement_'):]) # "срезаем" префикс, получаем id
    a = Announcement.objects.get(id=id)
    if a.sender.id != request.user.id:
        # не владелец => может только закрыть, не удалить
        remove_announcement(a.id, request.user)  # person can't delete (doesn't own), so just removes
    else:
        delete_announcement(a.id)


# собственно отображение основной страницы объявлений
@login_required
def show_announcements(request, edit=False):
    "display all announcements, probably trying to edit"

    header_handler(request) # обработка кнопок в верхней плашке

    user = request.user.concretize()
    viewed_ann = []
    form = None

    if user.role == models.profiles.Profile.LECT_ROLE:
        # отображение для преподов
        viewed_ann = Announcement.objects.all()  # lectors can see all anouncements

        if edit:
            # значит, создается новое объявление
            form = WriteLectorsForm()

            if request.method == "POST":
                form = WriteLectorsForm(request.POST)

                if form.is_valid():
                    inst = form.save(commit=False)

                    inst.sender = user # добавляем отправителя в полученное из формы объявление
                    inst.save()

                    # указываем получателей (в данном случае — все с выбранного курса)
                    inst.receivers.set(EmailUser.objects.filter(profile__course_number=request.POST['course_number']))
                    # due to the fact "course" is not model field,
                    # it is not auto-completed when creating form from request

                    return redirect('announce')

    # I use duplicating code due to the fact that lector/student behaviour may highly vary
    elif user.role == models.profiles.Profile.STUD_ROLE:
        # здесь пока дублируется код (см. пояснение выше), но это для того,
        # чтобы потом проще было настравать разную логику для студентов/преподов

        viewed_ann = user.recieved_announcements.all()

        if edit:
            form = WriteAnnounceForm()

            if request.method == "POST":
                form = WriteAnnounceForm(request.POST)

                if form.is_valid():
                    inst = form.save(commit=False)
                    # if course_id:
                    #     inst.course = CoursePage.objects.get(id=course_id).first()
                    inst.sender = user
                    inst.save()

                    inst.receivers.set(EmailUser.objects.filter(profile__course_number=user.profile.course_number))

                    return redirect('announce')

    else:
        raise PermissionDenied("You are not student/lecturer")

    return render(request, 'main/announcements.html', {'user': user,
                                                       'edit': edit,
                                                       'viewed_ann': viewed_ann,
                                                       'form': form, 'enable_mathjax': True})


# операции с БД запихнуты сюда же, хотя по-хорошему их лучше переместить в отдельный файл

def remove_announcement(ann_id, user):
    "removes user from recievers"
    ann = Announcement.objects.get(id=ann_id)
    ann.receivers.remove(user)

    if ann.receivers.count() == 0: # если объявление никто не видит…
        ann.delete() # …его не существует, верно?)


def delete_announcement(ann_id):
    Announcement.objects.get(id=ann_id).delete()


# view-шки, которые удалят и просто перенаправят к остальным объявлениям
# TODO: проблема с безопасностью, см. remove_material в course_views
@login_required
def remove_announcement_view(request, ann_id):
    header_handler(request)
    remove_announcement(ann_id, request.user)

    return redirect('announce')

@login_required
def delete_announcement_view(request, ann_id):
    "completely deletes announcement"
    header_handler(request)
    delete_announcement(ann_id)

    return redirect('announce')
