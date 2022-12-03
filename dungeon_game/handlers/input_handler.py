from dungeon_game.handlers.db_handler import DBHandler as db
from dungeon_game.handlers.print_handler import PrintHandler as ph

class InputHandler:

    @staticmethod
    def run_command(input):
        commands = InputHandler.parse_input(input)
        print(commands)
        for command in commands:
            if InputHandler.verify_command(command):
                print(command)

    @staticmethod
    def parse_input(input):
        '''receive string
            split string
            verify each word
            multiple commands? do all of them?'''
        return input.split()

    @staticmethod
    def verify_command(command):
        match command:
            case 'look' | 'l':
                ph.print_detailed_room()
            case 'inventory' | 'i':
                return True
            case 'get' | 'take':
                return True
            case 'north' | 'n':
                return True
            case 'west' | 'w':
                return True
            case 'south' | 's':
                return True
            case 'east' | 'e':
                return True