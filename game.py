from house import House

class Game:
    def __init__(self, player_name):
        self._player_name = player_name
        self.lives = 3
        self.items = []
        self.house = House()
        self.current_location = self.house.outside
        self.in_house = False

    def take_turn(self):
        print(self.current_location.read_message())
        direction = None
        while self.is_wrong(direction):
            direction = input(str("Where would you like to explore: ")).upper()



    def is_wrong(self, direction):
        return direction not in ["L", "R", "F", "B"]
