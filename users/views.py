# job_board/users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ProfileForm, UserRegistrationForm, ResumeForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user, defaults={})
    profile_form = ProfileForm(request.POST or None, instance=user_profile)

    if request.method == 'POST':
        if profile_form.is_valid():
            profile_form.save()

    return render(request, 'users/profile.html', {'user': user, 'user_profile': user_profile, 'profile_form': profile_form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        resume_form = ResumeForm(request.POST)
        if user_form.is_valid() and resume_form.is_valid():
            user = user_form.save()

            # Создаем UserProfile для нового пользователя
            user_profile, created = UserProfile.objects.get_or_create(user=user, defaults={})

            resume = resume_form.save(commit=False)
            resume.user_profile = user_profile
            resume.save()

            login(request, user)  # Автоматически войти после регистрации
            return redirect('users:profile')  # Перенаправление на страницу профиля пользователя
    else:
        user_form = UserRegistrationForm()
        resume_form = ResumeForm()
    return render(request, 'users/registration_form.html', {'user_form': user_form, 'resume_form': resume_form})