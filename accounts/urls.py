from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('register/', views.register, name = 'register'),
    path('activate/<uidb64>/<token>', views.activate, name = 'activate'),
    path('login/', views.login, name = 'login'),
    path('forgot_password/', views.forgot_password, name = 'forgot_password'),
    path('reset_password/', views.reset_password, name = 'reset_password'),
    path('reset_password_validate/<uidb64>/<token>', views.reset_password_validate, name = 'reset_password_validate'),
    path('logout/', views.logout, name = 'logout'),
]