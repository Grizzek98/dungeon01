

class Mob:

    def __init__(self, mob_type, name, max_health, atrributes, current_room=None):
        self.mob_type = mob_type
        self._name = name
        self._max_Health = max_health
        self._health = self._max_Health

        self._str = atrributes[0]
        self._dex = atrributes[1]
        self._vit = atrributes[2]
        self._cha = atrributes[3]
        self._mag = atrributes[4]

        self._current_room = current_room

        self.inventory = []

    def __repr__(self):
        return self._name

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @property
    def current_room(self):
        return self._current_room

    @current_room.setter
    def current_room(self, room):
        self._current_room = room
    

class Player(Mob):

    def __init__(self, mob_type, name, max_health, atrributes, current_room=None):
        super().__init__(mob_type, name, max_health, atrributes, current_room)


class Enemy(Mob):

    def __init__(self, mob_type, name, max_health, atrributes, current_room=None):
        super().__init__(mob_type, name, max_health, atrributes, current_room)