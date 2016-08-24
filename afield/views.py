from django.shortcuts import get_object_or_404, render
from .models import Room,RoomAction


def index(request, room_id=1, previous_room_action_id=0):
    room = get_object_or_404(Room, pk=room_id)
    room.roomaction_set.all()
    actiondescription =""
    if previous_room_action_id != 0:
        roomaction = get_object_or_404(RoomAction, pk=previous_room_action_id)
        actiondescription=roomaction.description

    return render(request, 'afield/index.html', {'room': room, 'actiondescription': actiondescription})


def about(request, room_id=1):
    room = get_object_or_404(Room, pk=7)
    room.roomaction_set.all()
    actiondescription =""
    return render(request, 'afield/index.html', {'room': room, 'actiondescription': actiondescription, 'returnroom':room_id})