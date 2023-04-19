from django.shortcuts import render
from django.http import HttpResponse
from .models import Resident
from .forms import ResidentForm

# Create your views here.
def greet_view(request):
    return render(request, 'index.html')

def dash_view(request):
    #resident = Resident.objects.get(pk=id)
    return render(request, 'dashboard.html')

def resident_list(request):
    pass

def resident_form(request):
    form = ResidentForm()
    
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form': form}
    return render(request, 'forms.html', context)