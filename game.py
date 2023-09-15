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
        self.page_count = 0

    def take_turn(self):
        if self.current_location.get_name() == "candle":
            self.candle()
            return
        elif self.current_location.get_name() == "candle_room":
            print("You try the door and it swings open! Inside the room is a lit candle that is glowing a bright " + self.house.check_candlelight() + " light.")
        elif self.current_location.get_name() == "library":
            self.library()
        elif self.current_location.get_name() == "vent":
            self.vent()
        elif self.current_location.get_name() == "chandelier":
            self.chandelier()
        elif self.current_location.get_name() == "ghost_room" and not self.house.ghost_room.check_open():
            print("You push on the door but it is way too heavy. \nYour arms get tired of pushing so you give up.")
            self.current_location = self.house.top_R
        elif self.current_location.get_name() == "balcony":
            if self.house.check_vent():
                print("You head over to the door and peer out the window.\nYou can see the huge forest that lies behind the"
                 " mansion.\nYou pull on the handle but the door is locked.\nYou try the key you used to enter the house"
                  " but no luck.")
                self.current_location = self.house.ghost_room
            else:
                self.balcony()
        elif self.current_location.get_name() == "gallery":
            self.gallery()
        else:
            print(self.current_location.read_message())
        if self.current_location.get_name() == "outside":
            print(self.current_location.read_message()) 
            self.front_doors()
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
        self.house.library.lock_door()
        self.house.gallery.lock_door()
        self.house.ghost_room.lock_door()
        while True:
            if not self.house.main_door.is_unlocked():
                print("Would you like to try your key?")
                unlock = input("Type Y to try, N to go back home: ").upper().strip()
                print()
                match unlock:
                    case "Y":
                        self.house.main_door.unlock()
                        print("The door opened and you head inside to check it out. \nYou walk into the mansion "
                              "and look around.\nThe door swings closed behind you and you know there is no point in trying to open it.")
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
                        print("The entryway looks the same as it did before.\nThe door swings closed behind you and "
                              "you know there is no point in trying to open it.")
                        self.current_location = self.house.porch
                        break
                    case "N":
                        print("You were too nervous and decided to head home instead. \nAll night you toss and turn,"
                              " wondering what is hidden behind the doors of that spooky house. \nThe next morning "
                              "you crawl out of bed and back to the house.")
                    case _:
                        self.wrong_answer()

    def candle(self):
        print("The candle sits on a pedestal with three buttons, a green, a blue, and a purple.\n"
              "What would you like to do?")
        while True:
            candle = input("Type G to press the green button, B for blue, P for purple, or E to go back: ").upper().strip()
            print()
            match candle:
                case "G":
                    self.house.library.unlock_door()
                    self.house.gallery.lock_door()
                    self.house.ghost_room.lock_door()
                    print("The candle glows bright green and you hear a noise from somewhere else in the house, "
                          "but you can't tell where it's coming from.\n")
                case "B":
                    self.house.library.lock_door()
                    self.house.gallery.lock_door()
                    self.house.ghost_room.unlock_door()
                    print("The candle glows bright blue and you hear a noise from somewhere else in the house, "
                          "but you can't tell where it's coming from.\n")
                case "P":
                    self.house.library.lock_door()
                    self.house.gallery.unlock_door()
                    self.house.ghost_room.lock_door()
                    print("The candle glows bright purple and you hear a noise from somewhere else in the house, "
                          "but you can't tell where it's coming from.\n")
                case "E":
                    self.current_location = self.house.bottom_L
                    break
                case _:
                    self.wrong_answer()

    def candle_room(self):
        print("You try the door and it swings open! Inside the room is a lit candle that is glowing a bright " + self.house.check_candlelight() + " light.")
    def wrong_answer(self):
        print("That's not one of the options. \nYou're so silly. \nPlease try again.")

    def library(self):
        if self.house.library.check_open():
            print("You push the door and it opens.\nInside the room is a huge library with shelves of books"
                  " that reach all the way to the ceiling. \nAs you explore the rows you find a bookshelf with"
                  " two books hanging out.")
            print("The books are titled 'The Secret to Solving a Maze' and 'History of Underground Monsters'\n"
                    "Would you like to read one?")
            while True:
                book = input("Type S to read about maze secrets, M to read about monsters, or B to leave the library: ").upper().strip()
                print()
                match book:
                    case "S":
                        print("You take the book off the shelf and start to read.\nIt's very interesting!")
                        if not self.house.book1.page_found():
                            print("As you flip through the pages, a sheet falls out onto the floor.\nIt has some weird scribbles"
                                  " on it.\nYou aren't sure what it means, but you put it in your pocket for later.")
                            self.house.book1.take_page()
                            if self.all_pages():
                                pass #TODO change mirror message
                    case "M":
                        print("You take the book off the shelf and start to read.\nIt's very interesting!\nThe book is about "
                              "an explorer who searched for evidence of monsters living under this very house.\nYou find his "
                              "research fascinating and you lean up against the book shelf as you read.\nAll of a sudden, "
                              "the bookshelves separate and you fall backwards into a pitfall :(")
                        self.lives -= 1
                        print("You now have "+str(self.lives)+" lives.")
                        self.current_location = self.house.outside
                        break
                    case "B":
                        self.current_location = self.house.top_L
                        print(self.current_location.read_message())
                        break
                    case _:
                        self.wrong_answer()
        else:
            print("You push on the door and it won't budge.")
            self.current_location = self.house.top_L


    def all_pages(self):
        return self.page_count == 4

    def chandelier(self):
        print("The chandelier glistens in front of you.\nHowever, the lights on one side aren't working.")
        if self.current_location.has_page():
            print("You spin the chandelier around to check it out, but you see nothing out of the ordinary.\n"
                  "You don't really know anything about electricity, so you leave it be.")
        else:
            print("You spin the chandelier around and you find that there is a piece of paper tucked into it!\n"
                  "The paper is covered in illegible scribbles, but you decide to hold onto it just in case.")
            self.current_location.take_page()
            if self.all_pages():
                pass #TODO change mirror message
        self.current_location = self.house.middle

    def vent(self):
        if self.current_location.bats():
            print("When you open the vent, a stream of bats come flying out and knock you to the ground.")
            self.lives -= 1
            print("You now have " + str(self.lives) + " lives.")
            self.current_location = self.house.outside
        elif self.current_location.has_key():
            print("You reach into the vent and pull out a key! \nThis must belong to a door somewhere.")
            self.current_location.take_key()
            self.current_location = self.house.top_R
        else:
            print("You poke around with your hand but the vent has already been emptied.")
            self.current_location = self.house.top_R

    def balcony(self):
            print("You try the key you found in the vent and the door opens!\nYou head outside onto the balcony "
                    "that overlooks the forest.")
            print("Out on the balcony you find a box similar to the one you found at the start of your adventure.")
            if self.current_location.has_page():
                print("You open the box and you find a tattered piece of paper.\nIt is so dirty you can barely make out"
                    " what is on it.\nJust in case, you tuck it away in your pocket.")
                self.current_location.take_page()
                if self.all_pages():
                    pass #TODO change mirror message
            else:
                print("You open the book to inspect it but you find that it is empty.\nMaybe you've checked it already, "
                    "or maybe its contents were stolen by the cat.")
            print("You take a minute to enjoy the beautiful view before heading back inside.")
            self.current_location = self.house.ghost_room
                
    def gallery(self):
        print("You pull the curtain aside to check what's behind it.")
        if self.house.gallery.check_open():
            print("There appears to be another room!\nYou enter the room to find a dark hallway lined with odd looking"
                    " portraits.\nThe whole room is lit with a purple light.")
            print("Two of the portraits stick out to you, one that depicts an vampire with teeth almost down to his chin, "
              "and one of a girl with an alligator lying across her shoulders. \nWould you like to take a closer look?")
        while True:
            picture = input("Type V to look at the vampire portrait, A to look at the girl with an alligator, or B to "
                            "exit the room: ").upper().strip()
            print()
            match picture:
                case "V":
                    if not self.house.portrait2.check_fallen():
                        if randint(0,1) == 1:
                            print("As you lean in to get a closer look at the portrait, you hear a creak, and then it falls on "
                                "top of you, and you get crushed.")
                            self.house.portrait2.fall_down()
                            self.lives -= 1
                            print("You now have " + str(self.lives) + " lives.")
                            self.current_location = self.house.outside
                            break
                    print("You take a closer look at the vampire.\nYou have no idea whether his teeth are real or fake, but "
                    "you can imagine they might make things difficult.")
                case"A":
                    print("The girl doesn't seem alarmed by the alligator, so you assume it must be her pet.")
                    if self.current_location.has_page():
                        print("Upon closer inspection you see that there is a piece of paper tucked into the top corner of"
                            "the frame.\nYou take it out and look at it.\nThe writing on it looks unreadable, and it is"
                            " too dark in the room to even try.\nYou tuck it into your pocket so you can give it a closer"
                            " look later.")
                        self.current_location.take_page()
                        if self.all_pages():
                            pass #TODO change mirror message
                case "B":
                        self.current_location = self.house.bottom_R
                        print(self.current_location.read_message())
                        break
                case _:
                    self.wrong_answer()


