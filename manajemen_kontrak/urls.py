from django.urls import path
from . import views

urlpatterns = [
    path('barang/', views.barang, name='barang')
]