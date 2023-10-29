from django.contrib import admin
#my imports
from apps.jobs import models

# Register your models here.
class BlogFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title', 'category')
    search_fields = ('title', 'category')

class CategoryFilterAdmin(admin.ModelAdmin):
    list_filter = ('title', )
    list_display = ('title',)
    search_fields = ('title',)
    

    
admin.site.register(models.Jobs, BlogFilterAdmin)
admin.site.register(models.Category, CategoryFilterAdmin)


