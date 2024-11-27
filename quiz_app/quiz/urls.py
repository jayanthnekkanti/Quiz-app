from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('quiz/', views.quiz, name='quiz'),
    path('reset/', views.reset, name='reset'),
]
