from django.urls import path
from . import views

urlpatterns = [
    path('show/ingredient', views.IngredientStock.as_view()),
    path('show/cup', views.CupStock.as_view()),
]
