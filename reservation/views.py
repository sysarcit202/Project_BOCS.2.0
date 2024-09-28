from django.shortcuts import render

# Create your views here.
def reservation(request):
    context = {
        'title': 'Project_BOCS | Reservation'
    }
    return render(request, 'reservation/reservation.html', context)


def patient(request):
    context = {
        'title': 'Project_BOCS | Patient'
    }
    return render(request, 'reservation/patient.html', context)

def reserv(request):
    context = {
        'title': 'Project_BOCS | Reservation'
    }
    return render(request, 'reservation/reserv.html', context)