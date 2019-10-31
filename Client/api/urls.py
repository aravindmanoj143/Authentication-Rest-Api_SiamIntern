from rest_framework import routers
from .views import Client_view
from django.urls import path
from . import views
urlpatterns = [

    path('<int:pk>/', views.Client_view .as_view()),
    path('auth/login/', views.LoginView.as_view()),
    path('auth/logout/', views.LogoutView.as_view()),


]