from django.urls import path
from . import views

urlpatterns = [
    path('refill/ing/<str:filter>', views.ReportRefillIngredientView.as_view()),
    path('refill/cup/<str:filter>', views.ReportRefillCupView.as_view()),
]