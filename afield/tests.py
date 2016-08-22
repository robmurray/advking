from django.test import TestCase

from .models import Room, RoomAction


class RoomMethodTests(TestCase):

    def test_Room(self):
        self.assertIs(True, True)
