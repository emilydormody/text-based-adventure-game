from house import House
from random import randint

class Game:
    def __init__(self, player_name):
        self._player_name = player_name
        self.lives = 3
        self.items = []
        self.house = House()
        self.current_location = None
        self.in_house = False

    def take_turn(self):
        if self.current_location.get_name() == "candle":
            self.candle_room()
            return
        self.current_location.read_message()
        while True:
            direction = input(str("Where would you like to explore: ")).upper()
            print()
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
                case _:
                    print("That's not one of the options. \nYou're so silly. \nPlease try again.")
        print(self.current_location.read_message())

    def game_start(self):
        print("In this game the commands are: L for left, R for right, F for forward and B for back. \nThis applies to all choices"
              " for walking and investigating objects unless stated otherwise. Enjoy!")
        print("\nWelcome " + self._player_name + ", it's time for an adventure! \nYou are walking home from "
                                       "school one day when you come across a cat up in a tree. \n"
                                       "Would you like to say hello?")
        while True:
            cat = input("Type Y to pet the cat, N to continue on your walk: ").upper().strip()
            print()
            match cat:
                case "Y":
                    print("The cat purrs, he is so happy :) \nYou discover that he's been sitting on a box, which "
                          "has been painted all black except for a gold clasp. \nYou open it up to reveal an old "
                          "and rusty key with an address on it. \nYou are familiar with the address, the house sits "
                          "at the end of your street. \nWhen you were younger you once tried to get inside, but the "
                          "doors were locked up tight. \nNow you appear to have the key! \nYou walk over to the "
                          "house to have a look.")
                    break
                case "N":
                    forgot = randint(0,5)
                    match forgot:
                        case 0: forgot = "headphones"
                        case 1: forgot = "sweater"
                        case 2: forgot = "textbook"
                        case 3: forgot = "phone charger"
                        case 4: forgot = "homework"
                    print("After ignoring the cat, you realized you left your " + forgot + " at school and have "
                                                                                       "to go back.")
                    print("On your walk home you see the cat is still there.")
                case _:
                    self.wrong_answer()
        self.front_doors()

    def front_doors(self):
        while True:
            if not self.house.main_door.is_unlocked():
                print("Would you like to try your key?")
                unlock = input("Type Y to try, N to go back home: ").upper().strip()
                print()
                match unlock:
                    case "Y":
                        self.house.main_door.unlock()
                        print("The door opened and you head inside to check it out. \nYou walk into the mansion "
                              "and look around.\nIn front of you is an empty space with a big chandelier hanging over it and a large mirror on the back wall." \
                       "\nOn your left and your right there are staircases, each of which have a door at both the top " \
                       "and the bottom and a landing halfway up. \nThe door swings closed behind you and you know there is no point in trying to open it.")
                        self.in_house = True
                        self.current_location = self.house.porch

                        break
                    case "N":
                        print("You were too nervous and decided to head home instead. \nAll night you toss and turn,"
                              " wondering what is hidden behind the doors of that spooky house. \nThe next morning "
                              "you crawl out of bed and back to the house.")
                    case _:
                        self.wrong_answer()

            else:
                print("Would you like to go back inside?")
                unlock = input("Type Y to head back inside, N to go home: ").upper().strip()
                print()
                match unlock:
                    case "Y":
                        print("The entryway looks the same as it did before.\nIn front of you is an empty space with a big chandelier hanging over it and a large mirror on the back wall." \
                       "\nOn your left and your right there are staircases, each of which have a door at both the top " \
                       "and the bottom and a landing halfway up. \nThe door swings closed behind you and you know there is no point in trying to open it.")
                        self.current_location = self.house.porch
                        break
                    case "N":
                        print("You were too nervous and decided to head home instead. \nAll night you toss and turn,"
                              " wondering what is hidden behind the doors of that spooky house. \nThe next morning "
                              "you crawl out of bed and back to the house.")
                    case _:
                        self.wrong_answer()

    def candle_room(self):
        print("The candle sits on a pedestal with three buttons, a green, a blue, and a purple.\n"
              "What would you like to do?")
        candle = input("Type G to press the green button, B for blue, P for purple, or B to go back: ").upper().strip()
        print()
        match candle:
            case "G":
                self.house.library.unlock_door()
                self.house.gallery.lock_door()
                self.house.ghost_room.lock_door()
                print("The candle glows bright green and you hear a noise from somewhere else in the house, "
                      "but you can't tell where it's coming from.")
            case "B":
                self.house.library.lock_door()
                self.house.gallery.lock_door()
                self.house.ghost_room.unlock_door()
                print("The candle glows bright blue and you hear a noise from somewhere else in the house, "
                      "but you can't tell where it's coming from.")
            case "P":
                self.house.library.lock_door()
                self.house.gallery.unlock_door()
                self.house.ghost_room.lock_door()
                print("The candle glows bright purple and you hear a noise from somewhere else in the house, "
                      "but you can't tell where it's coming from.")
            case "B":
                self.current_location = self.house.candle_room







































    def wrong_answer(self):
        print("That's not one of the options. \nYou're so silly. \nPlease try again.")


