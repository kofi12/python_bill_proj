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

#delete operation
def delete(request, id):
    resident = Resident.objects.get(id=id)
    resident.delete()
    return redirect('/')

#update operation
def update(request, id):
    if request == 'GET':
        resident = Resident.objects.get(id=id)
        form = ResidentForm(request.POST, instance=resident)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    return render(request, 'update.html', {'form': form})
    