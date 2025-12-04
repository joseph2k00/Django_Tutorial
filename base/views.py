from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'Room 1'},
    {'id': 2, 'name': 'Room 2'},
    {'id': 3, 'name': 'Room 3'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html', {
        'rooms': rooms,
    })    