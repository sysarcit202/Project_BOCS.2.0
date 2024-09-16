from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('reset', views.reset, name="reset"),
    path('signout', views.signout, name="signout"),
    path('activate/<uidb64>/<token>', views.activate, name="activate"),
]
