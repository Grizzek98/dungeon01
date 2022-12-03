from dungeon_game.item import *
from dungeon_game.handlers.db_handler import DBHandler as db

class ItemHandler:

    @staticmethod
    def create_item(name):
        item = tuple(db.fetch_item(name).fetchone())
        if item[0] == 'weapon':
            return Weapon(
                item[0],
                item[1],
                item[2],
                item[3],
                item[4],
            )
        if item[0] == 'consumable':
            return Consumable(
                item[0],
                item[1],
                item[2],
                item[5],
            )
        if item[0] == 'armor':
            return Armor(
                item[0],
                item[1],
                item[2],
                item[6],
            )
        else: return 'error'