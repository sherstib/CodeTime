from django.shortcuts import render
from django.utils import timezone
from .models import Lenguajes

def lenguajes_view(request):
    lenguajes = Lenguajes.objects.all()
    return render(request, 'program/lenguajes_list.html', {'lenguajes': lenguajes})
