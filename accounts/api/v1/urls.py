from . import views
from django.urls import path

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('reset-password-mail', views.send_email_password),
    path('reset-password-code', views.reset_password),
]
