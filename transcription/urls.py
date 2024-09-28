from django.urls import path
from . import views

urlpatterns = [
    path('', views.transcription, name="transcription"),
    path('transcrip/', views.transcrip, name="transcrip"),
]