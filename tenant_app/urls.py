from django.conf.urls import url
from django.urls import path
from tenant_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tenant_dashboard/', views.user_dashboard, name='tenant_dashboard'),
    path('admin_dashboard/', views.Admin_dashboard, name='admin_dashboard')

]
