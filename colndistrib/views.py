from django.shortcuts import render

# Create your views here.
def colndistrib(request):
    context = {
        'title': 'Project_BOCS | Collection & Distribution'
    }
    return render(request, 'colndistrib/colndistrib.html', context)

def collection(request):
    context = {
        'title': 'Project_BOCS | Collection'
    }
    return render(request, 'colndistrib/collection.html', context)

def distribution(request):
    context = {
        'title': 'Project_BOCS | Distribution'
    }
    return render(request, 'colndistrib/distribution.html', context)