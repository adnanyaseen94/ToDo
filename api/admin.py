from django.contrib import admin
from .models import ToDo, List, SubTask

# Register your models here.
admin.site.register(ToDo)
admin.site.register(List)
admin.site.register(SubTask)
