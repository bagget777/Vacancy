#job_board/vacancies/admin.py
from django.contrib import admin
from .models import Vacancy

admin.site.register(Vacancy)