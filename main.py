from game import Game

#name = input("Enter your player name: ")
g = Game("e")
g.game_start()
while g.in_house:
    g.take_turn()
g.end_game()