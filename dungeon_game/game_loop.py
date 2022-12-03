from dungeon_game.handlers.room_handler import RoomHandler as roomer
from dungeon_game.handlers.item_handler import ItemHandler as itemmer
from dungeon_game.handlers.mob_handler import MobHandler as mobber
from dungeon_game.handlers.print_handler import PrintHandler as printer
from dungeon_game.handlers.db_handler import DBHandler as db
from dungeon_game.handlers.input_handler import InputHandler as ih

class GameLoop():

    def __init__(self):
        db.initialize_db()
        self.room_handler = roomer()
        self.print_handler = printer()
        self.room_handler.construct_rooms()

        self.enemy = mobber.create_mob('zombie')
        self.player = mobber.create_player('grizzek')
        self.player.current_room = self.room_handler._rooms[0]

        # self.player.inventory.append(itemmer.create_item('sword'))
        # self.player.inventory.append(itemmer.create_item('health potion'))


    def game_loop(self):
        # printer.print_basic_state(self.player.current_room)
        # printer.print_inventory(self.player)
        # self.test_dict[('thing', 'thing1')]
        self.run_command(input())

    def run_command(self, input):
        for command in self.parse_input(input):
            print(command)
            self.verify_command(command)

    def parse_input(self, input):
        '''receive string
            split string
            verify each word
            multiple commands? do all of them?'''
        return input.split()

    # @staticmethod
    def verify_command(self, command):
        match command:
            case 'look' | 'l':
                printer.print_detailed_room(self.player.current_room)
            case 'inventory' | 'i':
                printer.print_inventory(self.player)
            case 'get' | 'take':
                return
            case 'north' | 'n':
                return True
            case 'west' | 'w':
                return True
            case 'south' | 's':
                return True
            case 'east' | 'e':
                return True


        # commands = InputHandler.parse_input(input)
        # print(commands)
        # for command in commands:
        #     if InputHandler.verify_command(command):
        #         print(command)

# class InputHandler:


