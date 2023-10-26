#job_board/vacancies/forms.py
from django import forms
from .models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'title',
            'company',
            'salary',
            'description',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'max_length': 200, 'min_length': 10}),
        }