from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Travel, Status
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
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
    return render(request, 'travels/details.html', {'travel': travel, 'title': "Travels Details Page", 'checking_form': checking_form, 'status': status_travel_doesnt_have})

def add_checking(request, travel_id):
    form = CheckingForm(request.POST)

    if form.is_valid():
        new_checking = form.save(commit=False)
        new_checking.travel_id = travel_id
        new_checking.save()
        return redirect('detail', travel_id = travel_id)

class  StatusList(ListView):
    model = Status

class StatusDetail(DetailView):
    model = Status

class StatusCreate(CreateView):
    model = Status
    fields = '__all__'

class StatusUpdate(UpdateView):
    model = Status
    fields = ['name', 'color']

class StatusDelete(DeleteView):
    model = Status
    success_url = '/status/'


def assoc_status(request, travel_id, status_id):
    Travel.objects.get(id=travel_id).travels.add(travel_id)
    return redirect('detail', travel_id = travel_id)


def unassoc_status(request, travel_id, status_id):
    Travel.objects.get(id=travel_id).status.remove(status_id)
    return redirect('detail', travel_id = travel_id)