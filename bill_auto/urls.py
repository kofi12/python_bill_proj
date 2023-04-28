from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_view),
    path('forms/', views.resident_form),
] 
