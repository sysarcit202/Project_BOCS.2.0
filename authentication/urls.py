from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('reset/', views.reset, name="reset"),
    path('insertuser/', views.insertuser, name='insertuser'),  
    path('signout/', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]

urlpatterns += staticfiles_urlpatterns()

