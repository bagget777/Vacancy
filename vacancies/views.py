#job_board/vacancies/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Vacancy
from .forms import VacancyForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def create_vacancy(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacancy_list')
    else:
        form = VacancyForm()
    return render(request, 'vacancies/create_vacancy.html', {'form': form})

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    paginator = Paginator(vacancies, 20)
    page = request.GET.get('page')

    try:
        vacancies = paginator.page(page)
    except PageNotAnInteger:
        vacancies = paginator.page(1)
    except EmptyPage:
        vacancies = paginator.page(paginator.num_pages)

    return render(request, 'vacancies/vacancy_list.html', {'vacancies': vacancies})

def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    return render(request, 'vacancies/vacancy_detail.html', {'vacancy': vacancy})


def home(request):
    return render(request, 'home.html')
