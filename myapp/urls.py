
from django.urls import path
from .import views

urlpatterns = [
    path('set/', views.setcookes),
    path('get/', views.getcookes),
    
]