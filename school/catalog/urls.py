from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.TeacherListView.as_view(), name='teachers'),
    path('teacher/<int:pk>', views.TeacherDetailView.as_view(), name='teacher-detail'),
    path('subjects/', views.SubjectListView.as_view(), name='subjects'),
    path('subject/<int:pk>', views.SubjectDetailView.as_view(), name='subject-detail'),
    path('myteachers/', views.MeetingTeachersByUserListView.as_view(), name='my-meetings'),
    path('reset_password/',auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
