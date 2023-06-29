from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='auth_login'),
    path('register', views.register, name='auth_register'),
    path('motdepasse_oublier', views.motdepasse_oublier, name='auth_motdepasse_oublier'),
    path('user_profile', views.user_profil, name='auth_user_profile'),
]