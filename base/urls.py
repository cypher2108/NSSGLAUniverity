from django.urls import path

from base import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student-registration/', views.user_input, name="userInput"),
    path('logout/', views.user_logout, name='logout'),
]