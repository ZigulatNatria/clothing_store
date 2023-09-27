from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import BaseRegisterView, LoginViewCustom, PasswordResetCustomView

urlpatterns = [
    path('login/',
         LoginViewCustom.as_view(template_name='sign/login.html'),
         name='login'),
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),
         name='logout'),
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='signup'),
    path('password-change/',
         PasswordChangeView.as_view(template_name='sign/password_change_form.html'), name='password_change'),
    path('password-change/done/',
         PasswordChangeDoneView.as_view(template_name='sign/password_change_done.html'), name='password_change_done'),
    # path('password-reset/',
    #      PasswordResetView.as_view(template_name='sign/password_reset_form.html'), name='password_reset'),
    path('password-reset/',
         PasswordResetCustomView.as_view(template_name='sign/password_reset_form.html',
                                         html_email_template_name='sign/password_reset_email.html'), name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name='sign/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='sign/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name='sign/password_reset_complete.html'), name='password_reset_complete'),
]