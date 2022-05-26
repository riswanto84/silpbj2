from django.shortcuts import render
from django.http import HttpResponse

def dashboard_kontrak(request):
    return render(request, 'manajemen_kontrak/dashboard_kontrak.html')
