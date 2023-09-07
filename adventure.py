#Happy Birthday darling
#I love you<3

from random import randint

class SpookyGame():
    def __init__(self):
        self.name = input("Enter your player name: ")
        self.player_lives = 3
        self.main_door_open = False
        self.tunnel_open = False
        self.library_open = False
        self.ghost_room_open = False
        self.portrait_room_open = False
        self.library_key_count = 0
        self.page1 = False
        self.page2 = False
        self.page3 = False
        self.page4 = False
        self.bats_out = False
        self.vent_key_found = False
        self.vent_count = 0
        self.push_count = 0
        self.vampire_attack = False

    def play(self):
        print("Welcome " + self.name + ", it's time for an adventure! \nYou are walking home from "
                                      "school one day when you come across a cat up in a tree. \n"
                                      "Would you like to say hello?")
        self.meet_cat()
        if self.player_lives == 0:
            print("You've ran out of lives and have to restart the game. Better luck next time.")
        else:
            print("Congratulations, you've beaten the game!")

    def meet_cat(self):
        cat = input("Type Y to pet the cat, N to continue on your walk: ").upper().strip()
        print()
        if cat == "Y":
            print("The cat purrs, he is so happy :) \nYou discover that he's been sitting on a box, which "
                  "has been painted all black except for a gold clasp. \nYou open it up to reveal an old "
                  "and rusty key with an address on it. \nYou are familiar with the address, the house sits "
                  "at the end of your street. \nWhen you were younger you once tried to get inside, but the "
                  "doors were locked up tight. \nNow you appear to have the key! \nYou walk over to the "
                  "house to give it a try.")
            self.house_doors()
        elif cat == "N":
            forgot = randint(0,5)
            if forgot == 0: forgot = "headphones"
            elif forgot == 1: forgot = "sweater"
            elif forgot == 2: forgot = "textbook"
            elif forgot == 3: forgot = "phone charger"
            elif forgot == 4: forgot = "homework"
            print("After ignoring the cat, you realized you left your " + forgot + " at school and have "
                                                                                   "to go back.")
            print("On your walk home you see the cat is still there.")
            self.meet_cat()
        else:
            self.wrong_answer()
            self.meet_cat()

    def house_doors(self):
        if self.main_door_open == False:
            print("Would you like to try your key?")
            unlock = input("Type Y to try, N to go back home: ").upper().strip()
            print()
            if unlock == "Y":
                self.main_door_open = True
                print("The door opened and you head inside to check it out. \nYou walk into the mansion "
                      "and look around. \nIn front of you is an empty space with a big chandelier "
                      "hanging over it and a large mirror on the back wall. \nOn your left and your right there are staircases, each of which "
                      "have a door at both the top and the bottom.")
                self.porch()
            elif unlock == "N":
                print("You were too nervous and decided to head home instead. \nAll night you toss and turn,"
                      " wondering what is hidden behind the doors of that spooky house. \nThe next morning "
                      "you crawl out of bed and back to the house.")
                self.house_doors()
            else:
                self.wrong_answer()
                self.house_doors()
        elif self.main_door_open == True:
            print("Would you like to go back inside?")
            unlock = input("Type Y to head back inside, N to go home: ").upper().strip()
            print()
            if unlock == "Y":
                print("The entryway looks the same as it did before.")
                self.porch()
            elif unlock == "N":
                print("You were too nervous and decided to head home instead. \nAll night you toss and turn,"
                      " wondering what is hidden behind the doors of that spooky house. \nThe next morning "
                      "you crawl out of bed and back to the house.")
                self.house_doors()
            else:
                self.wrong_answer()
                self.house_doors()

    def porch(self):
        print("You stand facing the mirror, where would you like to go?")
        walk = input("Type L to go left, R to go right, M to check out the mirror: ").upper().strip()
        print()
        if walk == "L":
            print("You're now at the foot of the stairs. \nIn front of you is a wooden door with a gold handle.")
            self.leftstairs_bottom()
        elif walk == "R":
            print("You head over the foot of the right staircase.\nIn front of you is a shimmery black curtain.")
            self.rightstairs_bottom()
        elif walk == "M":
            self.check_mirror()
        else:
            self.wrong_answer()
            self.porch()

    def leftstairs_bottom(self):
        print("Where would you like to go?")
        walk = input("Type D to try the door, S to go upstairs, E to go back to the entryway: ").upper().strip()
        print()
        if walk == "D":
            print("You try the door and it swings open!")
            print("Inside the room is a lit candle that is glowing " + self.light_colour() + " light.")
            self.candle()
        elif walk == "S":
            print("You climb the stairs and come across a big wooden door.")
            self.leftstairs_top()
        elif walk == "E":
            self.porch()
        else:
            self.wrong_answer()
            self.leftstairs_bottom()

    def rightstairs_bottom(self):
        print("What would you like to do?")
        curtain = input("Type C to check behind the curtain, S to go upstairs, or E to return to the entryway: ").upper().strip()
        print()
        if curtain == "C":
            print("You pull the curtain aside to check what's behind it.")
            if self.portrait_room_open:
                print("There appears to be another room!\nYou enter the room to find a dark hallway lined with odd looking"
                        " portraits.\nThe whole room is lit with a purple light.")
                self.portrait_room()
            elif not self.portrait_room_open:
                print("To your great disappointment, there is nothing behind the curtain but a wall.\nThe curtain must "
                        "just be for decoration.")
                self.rightstairs_bottom()
        elif curtain == "S":
                print("As you head up the stairs, the house gets darker and darker.\nAt the top of the stairs you come "
                      "across a steel door.\nIt looks very heavy.\nAbove the door there is a small vent that looks just big "
                      "enough for your hand to reach into.")
                self.rightstairs_top()
        elif curtain == "E":
            self.porch()
        else:
            self.wrong_answer()
            self.rightstairs_bottom()

    def check_mirror(self):
        self.check_tunnel()
        if self.tunnel_open == True:
            self.secret_tunnel()
        elif self.tunnel_open == False:
            print("You examine the mirror. \nIt is too dark to see your reflection properly, but it"
                  " appears to be a normal mirror. \nNothing special. \nYou return to the entryway.")
            self.porch()

    def candle(self):
        print("The candle sits on a pedestal with three buttons, a green, a blue, and a purple.\n"
              "What would you like to do?")
        candle = input("Type G to press the green button, B for blue, P for purple, or E to leave the room: ").upper().strip()
        print()
        if candle == "G":
            self.library_open = True
            self.portrait_room_open = False
            self.ghost_room_open = False
            self.library_key_count = 0
            print("The candle glows bright green and you hear a noise from somewhere else in the house, "
                  "but you can't tell where it's coming from.")
            self.candle()
        elif candle == "B":
            self.library_open = False
            self.portrait_room_open = False
            self.ghost_room_open = True
            self.library_key_count = 0
            print("The candle glows bright blue and you hear a noise from somewhere else in the house, "
                  "but you can't tell where it's coming from.")
            self.candle()
        elif candle == "P":
            self.library_open = False
            self.portrait_room_open = True
            self.ghost_room_open = False
            self.library_key_count = 0
            print("The candle glows bright purple and you hear a noise from somewhere else in the house, "
                  "but you can't tell where it's coming from.")
            self.candle()
        elif candle == "E":
            print("You exit the room and stand at the foot of the stairs.")
            self.leftstairs_bottom()
        else:
            self.wrong_answer()
            self.candle()

    def leftstairs_top(self):
        print("What would you like to do?")
        door = input("Type T to try the door, R to go right, or D to go down the stairs: ").upper().strip()
        print()
        if door == "T":
            if self.library_open:
                print("You push the door and it opens.\nInside the room is a huge library with shevlves of books"
                      " that reach all the way to the ceiling. \nAs you explore the rows you find a bookshelf with"
                      " two books hanging out.")
                self.library()
            else:
                print("You push on the door and it won't budge.\nWould you like to try your key?")
                key = input("Type Y to try your key, N to give up: ").upper().strip()
                print()
                if key == "Y":
                    self.library_key_count += 1
                    print("You can't find a key hole.")
                    if self.library_key_count > 3:
                        self.player_lives -= 1
                        print("Don't be stupid. \nYou know this won't work.\nLive count: " + str(self.player_lives))
                        if self.player_lives == 0:
                            return
                    self.leftstairs_top()
                if key == "N":
                    self.leftstairs_top()
                else:
                    self.wrong_answer()
                    self.leftstairs_top()
        elif door == "R":
            print("You follow the walkway and stand at a railing looking over the room you first entered when"
                  " you came into the house. \nThe chandelier is inches from your face.")
            self.middle()
        elif door == "D":
            print("You walk downstairs and find yourself in front of a door with a golden handle.")
            self.leftstairs_bottom()
        else:
            self.wrong_answer()
            self.leftstairs_top()

    def middle(self):
        print("What would you like to do?")
        walk = input("Type C to inspect the chandelier, L to go left or R to go right: ").upper().strip()
        print()
        if walk == "C":
            self.chandelier()
        elif walk == "L":
            print("You make your way along the hallway and come across a big wooden door.")
            self.leftstairs_top()
        elif walk == "R":
            print("You turn and continue to walk.\nAs you go the lights get dimmer and you come across a door made"
                  " of steel.\nIt looks very heavy.\nAbove the door there is a small vent that looks just big enough"
                  " for your hand to reach into.")
            self.rightstairs_top()
        else:
            self.wrong_answer()
            self.middle()

    def rightstairs_top(self):
        print("What would you like to do?")
        door = input("Type V to try the vent, D to try the door, L to go left, S to go downstairs: ").upper().strip()
        print()
        if door == "V":
            if not self.bats_out:
                if randint(0, 3) == 1:
                    print("When you open the vent, a stream of bats come flying out and knock you to the ground.")
                    self.bats_out = True
                    self.dead()
            self.bats_out = True
            if not self.vent_key_found:
                print("You reach into the vent and pull out a key! \nThis must belong to a door somewhere.")
                self.vent_key_found = True
                self.rightstairs_top()
            else:
                print("You poke around with your hand but the vent has already been emptied.")
                self.vent_count += 1
                if self.vent_count > 3:
                    print("When you open the vent, a stream of bats come flying out and knock you to the ground.")
                    self.dead()
                self.rightstairs_top()
        elif door == "D":
            if self.ghost_room_open:
                print("Even though the door looks heavy, manage to push it open quite easily.\nYou enter a room full"
                      " of white sheets, each of them with eyes drawn on, so that they look like ghosts hanging from "
                      "the ceiling.\nAt the back of the room you see another door with a round window in it.")
                self.ghost_room()
            else:
                print("You push on the door but it is way too heavy. \nYour arms get tired of pushing so you give up.")
                self.push_count += 1
                if self.push_count % 3 == 0:
                    print("Your arms are exhausted from trying the door.\nYou head down the stairs instead and come "
                          "across an opening covered by a shimmery black curtain.")
                    self.rightstairs_bottom()
                else:
                    self.rightstairs_top()
        elif door == "L":
            print("You head left.\nAs you approach the center of the mansion, the hallway seems to brighten.\nYou "
                  "stand looking over the room where you enter the house, with the chandelier in front of you.")
            self.middle()
        elif door == "S":
            print("You head down the stairs and come across a opening covered by a shimmery black curtain.")
            self.rightstairs_bottom()
        else:
            self.wrong_answer()
            self.rightstairs_top()

    def library(self):
        print("The books are titled 'The Secret to Solving a Maze' and 'History of Underground Monsters'\n"
              "Would you like to read one?")
        book = input("Type S to read about maze secrets, M to read about monsters, or E to leave the library: ").upper().strip()
        print()
        if book == "S":
            print("You take the book off the shelf and start to read.\nIt's very interesting!")
            if not self.page1:
                print("As you flip through the pages, a sheet falls out onto the floor.\nIt has some weird scribbles"
                      " on it.\nYou aren't sure what it means, but you put it in your pocket for later.")
                self.page1 = True
            self.library()
        elif book == "M":
            print("You take the book off the shelf and start to read.\nIt's very interesting!\nThe book is about "
                  "an explorer who searched for evidence of monsters living under this very house.\nYou find his "
                  "research fascinating and you lean up against the book shelf as you read.\nAll of a sudden, "
                  "the bookshelves separate and you fall backwards into a pitfall :(")
            self.dead()
        elif book == "E":
            print("You go back into the hallway.")
            self.leftstairs_top()
        else:
            self.wrong_answer()
            self.library()

    def chandelier(self):
        print("The chandelier glistens in front of you.\nHowever, the lights on one side aren't working.")
        if self.page2:
            print("You spin the chandelier around to check it out, but you see nothing out of the ordinary.\n"
                      "You don't really know anything about electricity, so you leave it be.")
            self.middle()
        elif not self.page2:
            print("You spin the chandelier around and you find that there is a piece of paper tucked into it!\n"
                  "The paper is covered in illegible scribbles, but you decide to hold onto it just in case.")
            self.page2 = True
            self.middle()

    def ghost_room(self):
        print("What would you like to do?")
        look = input("Type D to try the door, E to exit the room: ").upper().strip()
        print()
        if look == "D":
            print("You head over to the door and peer out the window.\nYou can see the huge forest that lies behind the"
                 " mansion.\nYou pull on the handle but the door is locked.\nYou try the key you used to enter the house"
                  " but no luck.")
            if self.vent_key_found:
                print("You try the key you found in the vent and the door opens!\nYou head outside onto the balcony "
                      "that overlooks the forest.")
                self.balcony()
            else:
                self.ghost_room()
        elif look == "E":
            print("You return to the hallway.")
            self.rightstairs_top()
        else:
            self.wrong_answer()
            self.ghost_room()

    def balcony(self):
        print("Out on the balcony you find a box similar to the one you found at the start of your adventure.")
        if not self.page3:
            print("You open the box and you find a tattered piece of paper.\nIt is so dirty you can barely make out"
                  " what is on it.\nJust in case, you tuck it away in your pocket.")
            self.page3 = True
        elif self.page3:
            print("You open the book to inspect it but you find that it is empty.\nMaybe you've checked it already, "
                  "or maybe its contents were stolen by the cat.")
        print("You take a minute to enjoy the beautiful view before heading back inside.")
        self.ghost_room()

    def portrait_room(self):
        print("Two of the portraits stick out to you, one that depicts an vampire with teeth almost down to his chin, "
              "and one of a girl with an alligator lying across her shoulders. \nWould you like to take a closer look?")
        picture = input("Type V to look at the vampire portrait, A to look at the girl with an alligator, or E to "
                        "exit the room: ").upper().strip()
        print()
        if picture == "V":
            if not self.vampire_attack:
                fall = randint(0,1)
                if fall == 1:
                    print("As you lean in to get a closer look at the portrait, you hear a creak, and then it falls on "
                          "top of you, and you get crushed.")
                    self.vampire_attack = True
                    self.dead()
            print("You take a closer look at the vampire.\nYou have no idea whether his teeth are real or fake, but "
                  "you can imagine they might make things difficult.")
            self.vampire_attack = True
            self.portrait_room()
        elif picture == "A":
            print("The girl doesn't seem alarmed by the alligator, so you assume it must be her pet.")
            if not self.page4:
                print("Upon closer inspection you see that there is a piece of paper tucked into the top corner of"
                      "the frame.\nYou take it out and look at it.\nThe writing on it looks unreadable, and it is"
                      " too dark in the room to even try.\nYou tuck it into your pocket so you can give it a closer"
                      " look later.")
                self.page4 = True
            self.portrait_room()
        elif picture == "E":
            print("You return to the hallway.")
            self.rightstairs_bottom()
        else:
            self.wrong_answer()
            self.portrait_room()

    def check_tunnel(self):
        if self.page1 and self.page2 and self.page3 and self.page4:
            self.tunnel_open = True
        return

    def secret_tunnel(self):
        print("The mirror doesn't look very much like a mirror.\nIn fact, it almost looks see through.\nYou look behind"
              " the mirror and you find a hidden tunnel!\nYou decide to crawl through and you find youself in a cave like"
              " room.\nThe room is empty except an open book sitting on a pedestal.\nYou are curious about the book and"
              " you flip through the pages.\nThey appear similar to the ones you've been collecting since you've been in"
              " the house.\nAt the end of the book you find that there appear to be pages ripped out.\nYou check the "
              "pages in your pockets to find they are a perfect match!\nThe book glows a bright light as the pages "
              "reattach themselves.\nThe writing becomes legible, and it tells you the story of the mansion you just "
              "explored.")
        return

    def light_colour(self):
        if self.library_open:
            return "green"
        elif self.ghost_room_open:
            return "blue"
        elif self.portrait_room_open:
            return "purple"
        else:
            return "white"

    def dead(self):
        self.player_lives -= 1
        print("\nUnfortunately you just died.\nBe more careful in the future, you only have "
              + str(self.player_lives)+" lives left.")
        print()
        if self.player_lives == 0:
            return
        else:
            print("You find yourself on the ground outside the house.")
            self.house_doors()

    def wrong_answer(self):
        print("That's not one of the options. \nYou're so silly. \nPlease try again.")
        return


def main():
    s = SpookyGame()
    s.play()

if __name__ == "__main__":
    main()
