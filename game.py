from player import Player
from utilities import Utilites
p1 = 0
p2 = 0
x = 0
i = 0

class Game:
    def __init__(self, p1, p2):
        pass
    

    
    Utilites.display_welcome()
    Utilites.display_rules()
    i = Utilites.choose_game_mode()
    print(i)
    
    
    
    
    
    
    
    #def run_game(self):
        #Utilites.display_welcome()
        #Utilites.display_rules()
        #self.battle()
        #Utilites.display_game_winner()

    #def battle(self):
        
        # instantiate one human player at least
        # p1 = Human()
        # Ask h vs h or h vs ai
        # instantiate second base upon response 
        # Conditional
        #     p2 = Human() or p2 = Robot()
            
        # p1.setname()
        # p2.setname()
    #    pass 

    #i = Utilites.choose_game_mode()
    #print(i)
    #keeplooping = True
    #while keeplooping :
    #    if i == 2:
            
    #        print('Player one please enter your name: ')
    #        p1 = Player.user_name(p1)
    #        print('Player two please enter your name: ')
    #        p2 = Player.user_name(p2)
    #        keeplooping = False
    #    elif i == 1:
            
    #        pass
    #    else:
    #        Utilites.choose_game_mode()
            
    