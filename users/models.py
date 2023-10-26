#job_board/users/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    other_fields = models.CharField(max_length=255)

class Resume(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    summary = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    # Добавьте другие поля резюме, такие как опыт работы, образование и навыки
