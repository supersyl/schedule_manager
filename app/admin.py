from django.contrib import admin
from app import models
# Register your models here.

class Task_admin(admin.ModelAdmin):
	list_display = ('priority','deadline','title','comment')
	list_filter = ('priority','deadline','title','comment')
	search_fields = ('priority','deadline','title','comment')

admin.site.register(models.Task)
