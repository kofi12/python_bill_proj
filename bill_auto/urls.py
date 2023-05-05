from django.urls import path
from . import views

urlpatterns = [
    path('', views.dash_view),
    path('update/', views.add, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
] 
