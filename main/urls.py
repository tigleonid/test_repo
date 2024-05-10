"""
Модуль, в котором регистрируются все ссылки
"""

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.course_views.index, name='home'),
    path('about-us', views.course_views.about, name='about'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('pages/<slug:slug>', views.course_views.course_page, name='pages'),
    path('pages/<slug:slug>/edit_general_info', views.course_views.course_page,
         {'edit_general_info': True}, name='pages_edit_general_info'),
    path('create_course', views.course_views.create_course, name='create_course'),
    path('profiles/<int:user_id>', views.profile_view.show_profile, name='profile'),
    path('profiles/<int:user_id>/edit', views.profile_view.show_profile, {'edit': True}, name='edit_profile'),
    path('announcements', views.announcement_view.show_announcements, name='announce'),
    path('announcements/edit', views.announcement_view.show_announcements, {'edit': True}, name='write_announce'),
    path('announcements/remove?<int:ann_id>', views.announcement_view.remove_announcement_view, name='remove_announce'),
    path('announcements/delete?<int:ann_id>', views.announcement_view.delete_announcement_view, name='delete_announce'),

    path('pages/markdown/create', views.markdown_page_view.create_page, name='create_markdown_page'),
    path('pages/markdown/<int:id>', views.markdown_page_view.view_page, name='view_markdown_page'),
    path('pages/markdown/<int:id>/edit', views.markdown_page_view.edit_page, name='edit_markdown_page'),

    path('pages/<slug:slug>/remove?<int:id>', views.course_views.remove_material, name='remove_material'),

]
