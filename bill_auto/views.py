from django.shortcuts import render
from django.http import HttpResponse
from .models import Resident

# Create your views here.
def greet_view(request):
    return render(request, 'index.html')

def dash_view(request, id):
    resident = Resident.objects.get(pk=id)
    return render(request, 'dashboard.html', {'resident': resident})