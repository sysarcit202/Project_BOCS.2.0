from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation, name="reservation"),
    path('reserv/', views.reserv, name="reserv"),
    path('patient/', views.patient, name="patient"),
]