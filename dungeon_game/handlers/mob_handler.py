from os import stat
from dungeon_game.mob import *
from dungeon_game.handlers.db_handler import DBHandler as db

class MobHandler:

    @staticmethod
    def create_mob(name):
        mob = tuple(db.fetch_mob(name).fetchone())
        if mob[0] == 'enemy':
            return Enemy(
                mob[0],
                mob[1],
                mob[2],
                [
                    mob[3],
                    mob[4],
                    mob[5],
                    mob[6],
                    mob[7],
                ])
        else: return 'error'

    @staticmethod
    def create_player(name):
        mob = tuple(db.fetch_mob('default_player').fetchone())
        return Player(
            mob[0],
            name,
            mob[2],
            [
                mob[3],
                mob[4],
                mob[5],
                mob[6],
                mob[7],
            ])