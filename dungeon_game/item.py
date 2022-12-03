import random

class Item:

    def __init__(self, item_type, name, weight):
        self._item_type = item_type # consumable, weapon, armor
        self._name = name
        self._weight = weight

    def __repr__(self):
        return self._name

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name


class Weapon(Item):

    def __init__(self, item_type, name, weight, damage, use_range):
        super().__init__(item_type, name, weight)
        self._damage = damage
        self._range = use_range

    def attack(self, mob):
        mob.health -= random.randint(1, self._damage)

class Consumable(Item):

    def __init__(self, item_type, name, weight, hp_gain):
        super().__init__(item_type, name, weight)
        self._hp_gain = hp_gain

    def consume(self, mob):
        mob.health += self._hp_gain

class Armor(Item):

    def __init__(self, item_type, name, weight, armor):
        super().__init__(item_type, weight, name)
        self._armor = armor