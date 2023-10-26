#job_board/vacancies/models.py
from django.db import models

class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

