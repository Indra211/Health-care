
from django.urls import path,include
from .views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView




urlpatterns = [
    path('', home, name='home'),
    path('user/register/', user_register, name='user_register'),
    path('accounts/login/', user_login, name='user_login'),
    path('user/logout/', user_logout, name='user_logout'),
    path('user/home/', user_home, name='user_home'),
    path('user/upload-report/', upload_report, name='upload_report'),
    path('accounts/view-reports/', view_reports, name='view_reports'),
    path('book-appointment/<int:pk>/',book_appointment, name='book_appointment'),
    path('book_appointment_save', book_appointment_save, name='book_appointment_save'),
    path('user/view-appointments/', view_appointments, name='view_appointments'),
    path('user/view-doctors/', view_doctors, name='view_doctors'),
    path('delete_selected_appointments/', delete_selected_appointments, name='delete_selected_appointments'),
    path('delete_selected_reports/', delete_selected_reports, name='delete_selected_reports'),
    path('update_profile/', update_profile, name='update_profile'),
    path('reset_password/', PasswordResetView.as_view(template_name='password_reset_form.html'), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]


