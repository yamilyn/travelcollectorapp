from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Travel, Checklist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import CheckingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import os

# Create your views here.

class TravelCreate(LoginRequiredMixin, CreateView):
    model = Travel
    fields = ['name', 'country', 'city', 'description', 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class TravelUpdate(LoginRequiredMixin, UpdateView):
    model = Travel
    fields = ['name', 'country', 'city', 'description', 'image']


class TravelDelete(LoginRequiredMixin, DeleteView):
    model = Travel
    success_url = '/travels/'


def home(request):
    os.getenv('NAME')
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def travels_index(request):
    travels = Travel.objects.filter(user = request.user)
    return render(request, 'travels/index.html', {'travels': travels})

@login_required
def travels_detail(request, travel_id):
    checking_form = CheckingForm
    travel = Travel.objects.get(id=travel_id)
    checklists_travel_for_planning = Checklist.objects.filter(user = request.user).exclude(id__in = travel.checklists.all().values_list('id'))
    return render(request, 'travels/details.html', {'travel': travel, 
    'title': "Travels Details Page", 'checking_form': checking_form, 
    'checklists': checklists_travel_for_planning})

@login_required
def add_checking(request, travel_id):
    form = CheckingForm(request.POST)

    if form.is_valid():
        new_checking = form.save(commit=False)
        new_checking.travel_id = travel_id
        new_checking.save()
        return redirect('detail', travel_id = travel_id)


class ChecklistDetail(LoginRequiredMixin, DetailView):
    model = Checklist

class ChecklistCreate(LoginRequiredMixin, CreateView):
    model = Checklist
    fields = ['name', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChecklistUpdate(LoginRequiredMixin, UpdateView):
    model = Checklist
    fields = ['name', 'description']

class ChecklistDelete(LoginRequiredMixin, DeleteView):
    model = Checklist
    success_url = '/checklists/'

@login_required
def checklists_index(request):
    checklists_list = Checklist.objects.filter(user = request.user)
    return render(request, 'main_app/checklist_list.html', {'checklists_list': checklists_list})

@login_required
def assoc_checklist(request, travel_id, checklist_id):
    Travel.objects.filter(user = request.user)
    Travel.objects.get(id=travel_id).checklists.add(checklist_id)
    return redirect('detail', travel_id = travel_id)

@login_required
def unassoc_checklist(request, travel_id, checklist_id):
    Travel.objects.filter(user = request.user)
    Travel.objects.get(id=travel_id).checklists.remove(checklist_id)
    return redirect('detail', travel_id = travel_id)


def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid signup, please check your password validation and try again.'

    form = UserCreationForm()
    ctx = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', ctx)