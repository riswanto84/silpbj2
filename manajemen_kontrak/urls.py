from django.urls import path
from . import views

urlpatterns = [
    path('dashboard_kontrak/', views.dashboard_kontrak, name='dashboard_kontrak')
]