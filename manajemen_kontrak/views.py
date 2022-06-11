from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard_kontrak(request):
    return render(request, 'manajemen_kontrak/dashboard_kontrak.html')

