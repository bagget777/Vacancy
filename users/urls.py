from django.urls import path
from users import views

app_name = 'users'  # Укажите пространство имен для приложения

urlpatterns = [
    # URL для регистрации пользователя
    path('register/', views.register, name='register'),
    # URL для просмотра профиля пользователя
    path('profile/', views.profile, name='profile'),
]
