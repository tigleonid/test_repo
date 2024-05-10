"""
Модуль, где регистрируются модели, которые будут отображатся в админке
"""

from django.contrib import admin
from .models import Profile, CoursePage, Material, Url, File, Video
from .models import EmailUser, StudentUser, LecturerUser
from .models import Announcement, MarkdownPage, MaterialContainer

from django.contrib.auth.admin import UserAdmin

UserAdmin.list_display = ('__str__', 'email')

admin.site.register(Profile)
admin.site.register(CoursePage)
admin.site.register(EmailUser, UserAdmin)
admin.site.register(StudentUser)
admin.site.register(LecturerUser)
admin.site.register(Material)
admin.site.register(Url)
admin.site.register(File)
admin.site.register(MaterialContainer)
admin.site.register(Announcement)
admin.site.register(Video)
admin.site.register(MarkdownPage)
