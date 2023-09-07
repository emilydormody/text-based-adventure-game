from house import House

class Game:
    def __init__(self, player_name):
        self._player_name = player_name
        self.lives = 3
        self.items = []
        self.house = House()
        self.current_location = self.house.outside
        self.in_house = True

    def take_turn(self):
        print(self.current_location._name)
        direction = None
        while True:
            print(self.current_location._name, self.current_location.get_left())
            direction = input(str("Where would you like to explore: ")).upper()
            match direction:
                case "L":
                    if self.current_location.get_left() is not None:
                        self.current_location = self.current_location.go_left()
                        break
                    else:
                        print("You can't go left here.")
                case "R":
                    if self.current_location.get_right() is not None:
                        self.current_location = self.current_location.go_right()
                        break
                    else:
                        print("You can't go right here.")
                case "F":
                    if self.current_location.get_forward() is not None:
                        self.current_location = self.current_location.go_forward()
                        break
                    else:
                        print("You can't go forward here.")
                case "B":
                    if self.current_location.get_back() is not None:
                        self.current_location = self.current_location.go_back()
                        break
                    else:
                        print("You can't go back here.")

