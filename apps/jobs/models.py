from django.db import models
from django_resized.forms import ResizedImageField 
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        
        
class Jobs(models.Model):
    category = models.ForeignKey(
        Category,on_delete=models.CASCADE,
        related_name="blog_category",
        verbose_name="Категории",
        blank=True,null=True
    )
    image = ResizedImageField(
        force_format="WEBP", 
        quality=100, 
        upload_to='jobs_image/',
        verbose_name="Фотография",
        blank = True, null = True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название ваканции"
    )
    descriptions = models.TextField(
        verbose_name="Описание ваканции"
    )
    responsiblities = RichTextField(
        verbose_name="Обязанности",
    )
    expectations = RichTextField(
        verbose_name="Ожидание",
    )
    experience = models.CharField(
        max_length=255,
        verbose_name="Опыт",
        blank=True, null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank = True, null = True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True, null=True
    )
    def __str__(self):
        return f"{self.title} - {self.category}"

    class Meta:
        verbose_name = "Ваканция"
        verbose_name_plural = "Ваканции"