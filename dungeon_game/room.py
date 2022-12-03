

class Room:

    def __init__(self, name, description, up, right, down, left, contents):
        self.name = name
        self.description = description
        self.connections = {
            "up": up,
            "right": right,
            "down": down,
            "left": left,
            }
        # self.up = up
        # self.right = right
        # self.down = down
        # self.left = left
        self.contents = contents
        self.visited = False

        def __str__(self):
            return self.name