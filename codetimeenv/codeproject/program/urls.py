from django.urls import path
from . import views

urlpatterns = [
    path('', views.lenguajes_view, name='lenguajes_view'),
]
