from django.contrib import admin
from .models import ReportRefillIngredient, ReportRefillCup
# Register your models here.


@admin.register(ReportRefillIngredient)
class ReportRefillIngredientAdmin(admin.ModelAdmin):
    list_display = ("user", "unit", "ingredient", "before", "after", "time")


@admin.register(ReportRefillCup)
class ReportRefillCupAdmin(admin.ModelAdmin):
    list_display = ("user", "unit", "cup", "before", "after", "time")
