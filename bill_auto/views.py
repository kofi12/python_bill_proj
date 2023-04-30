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
    name = request.POST['name']
    birthday = request.POST['birthday']
    admission_date = request.POST['admission_date']
    rent = request.POST['rent']
    
    resident = Resident(name=name, birthday=birthday, admission_date=admission_date, rent=rent)
    resident.save()
    return render(request, 'add.html')

#delete operation
def delete(request, id):
    resident = Resident.objects.get(id=id)
    resident.delete()
    return redirect('/')

#update operation
def update(request, id):
    resident = Resident.objects.get(id=id)
    
    return render(request, 'update.html', {'resident': resident})
    