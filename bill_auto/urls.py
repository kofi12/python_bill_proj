from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_view),
    path('forms/', views.add_resident),
    path('forms/<int:id>/', views.update_resident),
] 
