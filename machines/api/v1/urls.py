from django.urls import path
from . import views

urlpatterns = [
    path('sensor', views.SensorView.as_view()),
    path('timer', views.TimerView.as_view()),
    path('home', views.home),
]