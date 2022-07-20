from django.urls import path
from . import views

urlpatterns = [
    path('sensor', views.SensorView.as_view()),
    path('timer', views.TimerView.as_view()),
    path('home', views.home),
    path('unit', views.UnitView.as_view()),
    path('<str:operation>/ingredients/<int:unit_id>', views.IngredientUnitView.as_view()),
    path('<str:operation>/cups/<int:unit_id>', views.CupUnitView.as_view()),
]