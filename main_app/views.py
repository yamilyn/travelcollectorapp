from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Travel
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CheckingForm

# Create your views here.

class TravelCreate(CreateView):
    model = Travel
    fields = '__all__'
    

class TravelUpdate(UpdateView):
    model = Travel
    fields = '__all__'


class TravelDelete(DeleteView):
    model = Travel
    success_url = '/travels/'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def travels_index(request):
    travels = Travel.objects.all
    return render(request, 'travels/index.html', {'travels': travels})

def travels_detail(request, travel_id):
    checking_form = CheckingForm
    travel = Travel.objects.get(id=travel_id)
    return render(request, 'travels/details.html', {'travel': travel, 'title': "Travels Details Page", 'checking_form': checking_form})

def add_checking(request, travel_id):
    form = CheckingForm(request.POST)
    print(form)

    if form.is_valid():
        new_checking = form.save(commit=False)
        new_checking.travel_id = travel_id
        new_checking.save()
        return redirect('detail', travel_id = travel_id)