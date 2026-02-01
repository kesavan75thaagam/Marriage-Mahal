from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required

def PartialsView(request):
    return render(request, 'admin/Partials.html')

@login_required
def home_slider_view(request):
    return render(request, 'admin/home_slider.html')