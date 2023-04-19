from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resident
from .forms import ResidentForm

# Create your views here.
def greet_view(request):
    return render(request, 'index.html')

def dash_view(request):
    
    residents = Resident.objects.all().order_by('name')
    context = {'residents': residents}
    return render(request, 'dashboard.html', context)

def resident_form(request):
    form = ResidentForm()
    
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form': form}
    return render(request, 'forms.html', context)