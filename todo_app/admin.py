from django.contrib import admin

# Register your models here.
from todo_app.models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "completed", "created")
    list_filter = ("completed",)
    search_fields = ("title",)
admin.site.register(Task,TaskAdmin)