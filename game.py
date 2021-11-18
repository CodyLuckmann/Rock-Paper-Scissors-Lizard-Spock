from player import Player
from utilities import Utilites
from robot import Robot
#from test import Test
import sys
p1 = 0
p2 = 0
x = 0
z = 0
i = 0
counterp1 = 0
counterp2 = 0
counterAI = 0

class Game:
    def __init__(self, p1, p2):
        pass
    
#    def player_choice(self, p2c=None):
#        #Utilites.display_welcome()
#        player1_choice = 0
#        player2_choice = 0
#        if (player1_choice == 1 and player2_choice == 3 or 4):
#            player1_choice = True
#        elif (player1_choice == 2 and player2_choice == 1 or 5):
#            player1_choice = True
#        elif (player1_choice == 3 and player2_choice == 2 or 4):
#            player1_choice = True
#        elif (player1_choice == 4 and player2_choice == 5 or 2):
#            player1_choice = True
#        elif (player1_choice == 5 and player2_choice == 3 or 1):
#            player1_choice = True
#        elif player1_choice == player2_choice:
#            print('tie')
#            #need to ask the user input again
#        else:
#            player1_choice = False
    

    
    Utilites.display_welcome()
    Utilites.display_rules()
    i = Utilites.choose_game_mode()
    print(i)
    
    def game(self):
    
        while (counterp1 < 2) or (counterp2 < 2):
            if counterp1 == 2:
                print("Player 1 wins!") 
                sys(exit)
            elif counterp2 == 2:
                print("Player 2 wins!")
                sys(exit)
            elif i == 1:
                x = Player.display_and_pick_gestures(x)
                z = Robot.display_and_pick_gestures(Player.robolist)
                print(x)
                print(z)
            elif i == 2:
                print('Player one choose first')
                x = Player.display_and_pick_gestures(x)
                print('Player two choose')
                z = Player.display_and_pick_gestures(z)
                print('Player one chose')
                print(x)
                print('Player two chose')
                print(z)
                if ((x == 1) and ((z == 3) or (z == 4))):
                    print(counterp1)
                    counterp1 = counterp1 + 1
                    print(counterp1)
                elif ((x == 2) and ((z == 1) or (z == 5))):
                    print(counterp1)
                    counterp1 = counterp1 + 1
                    print(counterp1)
                elif ((x == 3) and ((z == 2) or (z == 4))):
                    print(counterp1)
                    counterp1 = counterp1 + 1
                    print(counterp1)
                elif ((x == 4) and ((z == 5) or (z == 2))):
                    print(counterp1)
                    counterp1 = counterp1 + 1
                    print(counterp1)
                elif ((x == 5) and ((z == 3) or (z == 1))):
                    print(counterp1)
                    counterp1 = counterp1 + 1
                    print(counterp1)
                elif x == z:
                    print('tie')
                    #need to ask the user input again
                else:
                    counterp2 = counterp2 + 1
                    print(counterp2)
            
            
            
    
        
    
    
    
    
    
    
    
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
            
    