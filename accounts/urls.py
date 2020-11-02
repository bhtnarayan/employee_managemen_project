from django.urls import path, include
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'registration/logout.html'), name = "logout"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'registration/password_change.html'), name = "password_change"),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'registration/change_password_done.html')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset.html'), name = "password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_sent.html')),
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_ok.html')),
    path('password_reset/complete/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_cmplte.html')),
    path('register/', views.register, name = "register"),
    path('profile/', views.profile, name = "profile"),
    path('profile/edit/', views.edit_profile, name = "edit_profile"),
]
