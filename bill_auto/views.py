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

#create operation
def add_resident(request):
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ResidentForm()
        
    context = {'form': form}
    return render(request, 'forms.html', context)

#delete operation
def delete_resident(request, id):
    resident = Resident.objects.get(id=id)
    if request.method == 'DELETE':
        resident.delete()
        return redirect('/')

#update operation
def update_resident(request, id):
    resident = Resident.objects.get(id=id)
    
    if request.method == 'POST':
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ResidentForm(instance=resident)
    
    context = {'form': form}
    return render(request, 'forms.html', context)
    