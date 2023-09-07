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
        while True:
            direction = input(str("Where would you like to explore: ")).upper()
            match direction:
                case "L":
                    if self.current_location.get_left() is not None:
                        self.current_location = self.current_location.go_left()
                    else:
                        print("You can't go left here.")
                case "R":
                    if self.current_location.get_right() is not None:
                        self.current_location = self.current_location.go_right()
                    else:
                        print("You can't go right here.")
                case "F":
                    if self.current_location.get_forward() is not None:
                        self.current_location = self.current_location.go_forward()
                    else:
                        print("You can't go forward here.")
                case "B":
                    if self.current_location.get_back() is not None:
                        self.current_location = self.current_location.go_back()
                    else:
                        print("You can't go back here.")



    def is_wrong(self, direction):
        return direction not in ["L", "R", "F", "B"]
