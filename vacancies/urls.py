#job_board/vacancies/urls.py
from django.urls import path
from . import views

app_name = 'vacancies'

urlpatterns = [
    path('vacancy_list/', views.vacancy_list, name='vacancy_list'),
    path('vacancy/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
    path('create_vacancy/', views.create_vacancy, name='create_vacancy'),
    path('', views.home, name='home'),
]