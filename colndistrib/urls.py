from django.urls import path
from . import views

urlpatterns = [
    path('', views.collection, name="collection"),
    path('colndistrib/', views.colndistrib, name="colndistrib"),
    path('distribution/', views.distribution, name="distribution"),
]