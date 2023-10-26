"""
URL configuration for job_board project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#job_board/urls.py
from django.contrib import admin
from django.urls import path, include  # Импортируем include
from allauth.account.views import SignupView






urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('vacancies/', include('vacancies.urls')),
    path('accounts/signup/',SignupView.as_view(), name='account_signup'),
    path('accounts/', include('allauth.urls')),  # URL-шаблоны allauth для управления аутентификацией
]


