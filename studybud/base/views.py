from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm
rooms=[
    {'id': 1, 'name': 'room1'},
    {'id': 2, 'name': 'room2'},
    {'id': 3, 'name': 'room3'}
]
rooms=Room.objects.all()
def home(request):
    return render(request, 'base/home.html',{'rooms':rooms})

def room(request, pk):
    room=Room.objects.get(id=pk)
    context={'room':room}
    return render(request,'base/room.html',context)

def create_room(request):
    form=RoomForm()
    if request.method == 'POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)


def edit_room(request,pk):
    room=Room.objects.get(id=int(pk))
    form=RoomForm(instance=room)
    if request.method == 'POST':
        form=RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)




def delete_room(request,pk):
    room=Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})