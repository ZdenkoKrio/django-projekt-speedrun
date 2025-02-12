from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Band
from .forms import BandForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Account created for {user.username}!")
            return redirect('band-list')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class BandListView(ListView):
    model = Band
    template_name = 'band_list.html'
    context_object_name = 'bands'

class BandDetailView(DetailView):
    model = Band
    template_name = 'band_detail.html'
    context_object_name = 'band'

class BandCreateView(LoginRequiredMixin, CreateView):
    model = Band
    form_class = BandForm
    template_name = 'band_form.html'
    success_url = reverse_lazy('band-list')

class BandUpdateView(LoginRequiredMixin, UpdateView):
    model = Band
    form_class = BandForm
    template_name = 'band_form.html'
    success_url = reverse_lazy('band-list')

class BandDeleteView(LoginRequiredMixin, DeleteView):
    model = Band
    template_name = 'band_confirm_delete.html'
    success_url = reverse_lazy('band-list')