from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupFunc, name="sns_signup"),
    path('login/', views.loginFunc, name='sns_login'),
    path('logout/', views.logoutFunc, name='sns_logout'),
    path('list/', views.listFunc, name='sns_list'),
    path("detail/<int:pk>/", views.detailFunc, name="sns_detail"),
    path("good/<int:pk>/", views.goodFunc, name="sns_good"),
    path("read/<int:pk>", views.readFunc, name="sns_read")
]
