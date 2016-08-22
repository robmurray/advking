from django.db import models
from datetime import datetime


class Room(models.Model):
    name = models.CharField(max_length=50,default="")
    description = models.TextField(max_length=1000,default="")
    createDate = models.DateTimeField('date created',default=datetime.now, blank=True)

    def __str__(self):
        return self.description


class RoomAction(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    nextRoom = models.IntegerField(default=0)
    # nextRoom = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="nextRoom")
    name = models.CharField(max_length=50,default="")
    description = models.TextField(max_length=1000,default="", blank=True)
    createDate = models.DateTimeField('date created',default=datetime.now, blank=True)

    def __str__(self):
        return self.description
