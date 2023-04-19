from django.urls import path
from . import views

urlpatterns = [
    path('', views.greet_view),
    path('dashboard/', views.dash_view),
    path('forms/', views.resident_form),
] 