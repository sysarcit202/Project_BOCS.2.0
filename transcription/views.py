from django.shortcuts import render

# Create your views here.
def transcrip(request):
    context = {
        'title': 'Project_BOCS | Transcription'
    }
    return render(request, 'transcription/transcrip.html', context)

def transcription(request):
    context = {
        'title': 'Project_BOCS | Transcription'
    }
    return render(request, 'transcription/transcription.html', context)