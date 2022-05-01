from django.urls import path

from dashboard import views

urlpatterns = [
    path('dashboard/', views.dashboard_home, name='dashboard-home'),
    path('dashboard/application-request', views.dashboard_application_request, name='dashboard-application-request'),
    path('dashboard/application-request-accept', views.accept_application, name='accept-application'),
    path('dashboard/application-request-reject', views.reject_application, name='reject-application'),
]