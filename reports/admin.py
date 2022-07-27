from django.contrib import admin
from .models import ReportRefill
# Register your models here.


@admin.register(ReportRefill)
class ReportRefillIngredientAdmin(admin.ModelAdmin):
    list_display = ("user", "unit", "ingredient", "cup", "before", "after", "time")

