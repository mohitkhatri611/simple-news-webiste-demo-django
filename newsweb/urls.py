from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='business'),
    path('tech/',views.tech, name='tech')
]
