from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Resident
from .forms import ResidentForm

# Create your views here.

def dash_view(request):
    
    residents = Resident.objects.all().order_by('name')
    context = {'residents': residents}
    return render(request, 'dashboard.html', context)

#create operation
def add(request):
    form = ResidentForm()
    
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    
    return render(request, 'update.html', context)

#delete operation
def delete(request, id):
    resident = Resident.objects.get(id=id)
    resident.delete()
    return redirect('/')

#update operation
def update(request, id):
    resident = Resident.objects.get(id=id)
    form = ResidentForm(instance=resident)
    
    if request.method == 'POST':
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    
    return render(request, 'update.html', context)
    