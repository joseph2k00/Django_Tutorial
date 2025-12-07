from django.shortcuts import render
from .models import Room

def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {
        'rooms': rooms,
    })    

def room(request, pk):
    r = Room.objects.get(id=pk)

    return render(request, 'base/room.html', {
        'room': r
    })