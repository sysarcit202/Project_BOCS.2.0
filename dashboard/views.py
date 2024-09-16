from django.shortcuts import render

# Create your views here.
def dashboard(request):
    context = {
        'title': 'Project_BOCS | Dashboard'
    }
    return render(request, 'dashboard/dashboard.html', context)

