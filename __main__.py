from dungeon_game.game_loop import GameLoop
from dungeon_game.handlers.db_handler import DBHandler

def main():
    game_loop = GameLoop()
    game_loop.game_loop()

if __name__ == '__main__':
    main()