class MessageHandler:
    def __init__(self):
        pass

    def set_message(self, obj):
        match obj:
            case "porch":
                return "In front of you is an empty space with a big chandelier hanging over it and a large mirror on the back wall." \
                       "\nOn your left and your right there are staircases, each of which have a door at both the top " \
                       "and the bottom and a landing halfway up."
            case "bottom_L":
                return "You walk to the landing between the sets of stairs. \nTo your left is a wooden door with a gold handle and on your" \
                       " right is the room where you first entered the house. \nIn front of you is a set of stairs heading further up."
            case "bottom_R":
                return "You take the stairs until you reach the landing.\nTo your right is a shimmery black curtain, " \
                       "and on your left is the room where you first entered the house. \nIn front of you is a set of stairs. It is dark but " \
                       "they appear to head upwards."
            case "top_L":
                return "As you continue through the house, you come across a big wooden door in front of you. \nThe steps downward " \
                       "are behind you and there is a hallway to your right."
            case "top_R":
                return "As you walk, the house gets darker and darker.\nEventually you end up facing "\
                      "a steel door. It looks very heavy.\nTo your right there is a small vent that looks just big "\
                      "enough for your hand to reach into.\nThe steps downward are behind you and there is a hallway to your left."
            case "middle":
                return "You follow the hallway and come to at a railing looking over the room you first entered when"\
                  " you came into the house. \nBehind you there is a chandelier, hanging over the center of the house. \n" \
                       "The hallway continues to the left and the right, but the right is significantly darker."




