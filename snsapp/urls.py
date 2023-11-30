from django.urls import path
from . import views

urlpatterns = [
    path('', views.getSns),
    path('signup/', views.signupFunc, name="sns_signup")
]
