from django.shortcuts import render

# Create your views here.
def sumrep(request):
    context = {
        'title': 'Project_BOCS | Summary Report'
    }
    return render(request, 'sumrep/sumrep.html', context)