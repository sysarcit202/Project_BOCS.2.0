from django.shortcuts import render

# Create your views here.
def inventory(request):
    context = {
        'title': 'Project_BOCS | Inventory',
        'navtitle': 'INVENTORY',
    }
    return render(request, 'inventory/inventory.html', context)

def donor(request):
    context = {
        'title': 'Project_BOCS | Donor',
        'navtitle': 'DONOR',
    }
    return render(request, 'inventory/donor.html', context)

def instock(request):
    context = {
        'title': 'Project_BOCS | In-Stock',
        'navtitle': 'IN-STOCK',
    }
    return render(request, 'inventory/instock.html', context)

def used(request):
    context = {
        'title': 'Project_BOCS | Used',
        'navtitle': 'USED',
    }
    return render(request, 'inventory/used.html', context)