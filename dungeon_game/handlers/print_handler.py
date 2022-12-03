


class PrintHandler:

    @staticmethod
    def print_basic_state(current_room):
        PrintHandler.print_basic_room(current_room)
        if len(current_room.contents) > 0:
            print('\n---Items in this room---')
            for item in current_room.contents:
                print(f'| {item}')

    @staticmethod
    def print_inventory(thing):
        if len(thing.inventory) > 0:
            print(f"\n---{thing}'s inventory---")
            for item in thing.inventory:
                print(f'| {item}')
        else: print(f"{thing}'s inventory is empty")

    @staticmethod
    def print_basic_room(current_room):
        print(f'---{current_room.name}---')
        print(f'{current_room.description}')

    @staticmethod
    def print_detailed_room(current_room):
        print(f'---{current_room.name}---')
        print(f'{current_room.description}')
        if len(current_room.contents) > 0:
            print('\n---Items in this room---')
            for item in current_room.contents:
                print(f'| {item}')
