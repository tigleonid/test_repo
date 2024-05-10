from django.urls import path

from .views import StudentSignUpView, LecturerSignUpView

urlpatterns = [
    path('signup/student', StudentSignUpView.as_view(), name='s_signup'),
    path('signup/lecturer', LecturerSignUpView.as_view(), name='l_signup'),
]
