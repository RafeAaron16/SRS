from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('login', views.login, name='login'),
path('signup', views.signup, name='signup'),
path('verification', views.verification, name='verification'),
path('verifynew', views.verifynew, name='verifynew'),
path('main', views.main, name='main')
]
