from django.shortcuts import render
from django.http import HttpResponse
from .models import Travel
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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
    travel = Travel.objects.get(id=travel_id)
    return render(request, 'travels/details.html', {'travel': travel, 'title': "Travels Details Page"})