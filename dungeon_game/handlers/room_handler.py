import dungeon_game.constants as c
from dungeon_game.room import Room
import json as j

class RoomHandler:

    def __init__(self):
        self._rooms = []

    def construct_rooms(self):
        self.f = open(c.ROOM_INFO_PATH)
        self.room_data = j.load(self.f)
        for r in self.room_data['room']:
            room = Room(
                r['name'], 
                r['description'],
                r['up'],
                r['right'],
                r['down'],
                r['left'],
                r['contents'],)
            self._rooms.append(room)
        self._connect_rooms()
        self.f.close()
    
    def _connect_rooms(self):
        for room in self._rooms:
            for conn in room.connections.items():
                if conn[1] != 'None':
                    for other_room in self._rooms:
                        if conn[1] == other_room.connections[conn[0]]:
                            room.connections[conn[0]] = other_room

    def print_rooms(self):
        for room in self._rooms:
            print(room.name)
            for conn in room.connections.items():
                print(conn)
