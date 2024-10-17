from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.inventory, name="inventory"),
    path('instock/', views.instock, name="instock"),
    path('used/', views.used, name="used"),
    path('donor/', views.donor, name="donor"),
    path('insertuser/', views.insertuser, name='insertuser'),
]

urlpatterns += staticfiles_urlpatterns()