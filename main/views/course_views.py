"""
Отображение страниц главной страницы и курсов
"""

from django.shortcuts import render, redirect, get_object_or_404
from ..models import CoursePage, Material
from ..forms import CreateCourseForm, EditCourseGeneralInfo
from ..forms import ContainerForm
from django.contrib.auth.decorators import login_required

from ..models import MaterialContainer
from ..models import Profile, MarkdownPage

from .announcement_view import header_handler
from ..other.markdown import generate_html


# главная страница
@login_required
def index(request):
    header_handler(request) # обязательный метод для обработки кнопок в "шапке" сайта
    courses = CoursePage.objects.all()

    # просто передаем нужные объекты в Template,
    # он сам за нас все отрендерит
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта',
                   'courses': courses,
                   'markdown_pages': MarkdownPage.objects.all()}) 


# страница "о сайте", доступная всем
def about(request):
    header_handler(request)
    return render(request, 'main/about.html')

# страница курса
@login_required
def course_page(request, slug, edit_general_info=False):
    header_handler(request)
    page = get_object_or_404(CoursePage, slug=slug) # получаем курс

    if edit_general_info: # режим редактирования
        edit_general_info = EditCourseGeneralInfo(instance=page) # создаем форму

        if request.method == "POST" and 'edit_general_info' in request.POST: # редактируется общая информация
            form = EditCourseGeneralInfo(request.POST, request.FILES, instance=page)

            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('pages', slug)

    if request.method == 'POST' and 'edit_material_submit' in request.POST: # добавляются материалы
        edit_material_form = ContainerForm(request.POST, request.FILES)
        # there I'm using same name for bool of state (editing/not) and form, because bool(form) == True

        if edit_material_form.is_valid():
            role = request.user.concretize().role
            # сохраняем в соотв. роли блоке
            edit_material_form.save(parent=(page.student_block if role == Profile.STUD_ROLE else page.lecturer_block))
            return redirect(request.build_absolute_uri()) # перезагружаемся (redirect на тот же uri)
    else:
        edit_material_form = ContainerForm() # создаем форму для добавления материалов

    return render(request, 'main/course_page.html', {'page': page,
                                                     'edit_general_info': edit_general_info,
                                                     'edit_material_form': edit_material_form,
                                                     'enable_mathjax': True})

@login_required
def remove_material(request, slug, id):
    # TODO: сейчас любой материал может удалить любой человек, если перейдет по нужной ссылке
    # для безопасности здесь нужны проверки, есть ли у удалятеля права удалять
    # альтернативный вариант — сделать удаление POST-запросом (через форму)
    Material.objects.get(id=id).delete()
    return redirect('pages', slug)


# создание нового курса
@login_required
def create_course(request):
    header_handler(request)

    # простейшая view для заполнения формы,
    # можно потом будет навешать дополнительных вкусностей

    error = ''
    if request.method == 'POST': # получаем готовую форму
        form = CreateCourseForm(request.POST) # воссоздаем форму из параметров запроса

        if form.is_valid():
             # commit=False — не до конца сохраняем,
             # т.к. нам надо подредактировать объект формы
            instance = form.save(commit=False)
            instance.create_slug() # редактируем — генерируем имя-ссылку (slug)
            instance.save()

            return redirect('home')
        else:
            error = 'Ошибка'

    form = CreateCourseForm() # создаем пустую форму

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_course.html', context)
