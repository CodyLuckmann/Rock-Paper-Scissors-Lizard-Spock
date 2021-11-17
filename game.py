from player import Player
from utilities import Utilites
p1 = 0
p2 = 0
x = 0

class Game:
    def __init__(self, p1, p2):
        pass
    
   

    Utilites.display_welcome()
    Utilites.display_rules()
    i = Player.choose_game_mode(x,x)
    print(i)
    while i != 1 or 2:
        if i == 2:
            print('Player one please enter your name: ')
            p1 = Player.user_name(p1)
            print('Player two please enter your name: ')
            p2 = Player.user_name(p2)
        elif i == 1:
            i = i
        else:
            Player.choose_game_mode(x, x)
    
