from django.shortcuts import render
from django.http import HttpResponse

def barang(request):
    return HttpResponse('data barang')
