from django.shortcuts import redirect, render
from django.contrib import messages
from django.db import transaction, IntegrityError 

def dashboard(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)

def update(request):
    context = {
        'title': 'Update'
    }
    return render(request, 'dashboard/update.html', context)
