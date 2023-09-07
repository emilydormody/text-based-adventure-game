from game import Game

#name = input("Enter your player name: ")
g = Game("e")
while g.in_house:
    g.take_turn()