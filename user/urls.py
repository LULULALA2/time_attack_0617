from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignApiView.as_view()),

    path('login/', views.UserApiView.as_view()),
    path('logout/', views.UserApiView.as_view())
]
