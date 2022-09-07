from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    list_display_links = ('id',)
    search_fields = ('title',)


admin.site.register(Task, TaskAdmin)



