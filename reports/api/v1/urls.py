from django.urls import path
from . import views

urlpatterns = [
    path('refill/<str:filter>', views.ReportRefillIngredientView.as_view()),
]