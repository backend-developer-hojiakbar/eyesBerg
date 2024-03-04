from django.contrib import admin
from .models import Cleaner
# Register your models here.
@admin.register(Cleaner)
class CleanerAdmin(admin.ModelAdmin):
    list_display = ['first_name']
