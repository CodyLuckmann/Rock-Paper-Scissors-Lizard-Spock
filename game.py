from player import Player
from utilities import Utilites
from robot import Robot
import sys

class Game:
    def __init__(self):
        pass
    
  

    
    Utilites.display_welcome()
    Utilites.display_rules()

    
    def game(i):
        x = 0
        z = 0
        counterp1 = 0
        counterp2 = 0
    
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
                # print(x)
                # print(z)
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
                    counterp1 = counterp1 + 1
                    print("Player one wins this round")
            elif ((x == 2) and ((z == 1) or (z == 5))):
                    counterp1 = counterp1 + 1
                    print("Player one wins this round")
            elif ((x == 3) and ((z == 2) or (z == 4))):
                    counterp1 = counterp1 + 1
                    print("Player one wins this round")
            elif ((x == 4) and ((z == 5) or (z == 2))):
                    counterp1 = counterp1 + 1
                    print("Player one wins this round")
            elif ((x == 5) and ((z == 3) or (z == 1))):
                    counterp1 = counterp1 + 1
                    print("Player one wins this round")
            elif x == z:
                    print('tie')
                    
            else:
                    counterp2 = counterp2 + 1
                    print("Player two wins this round")
            
            
            
    
        
    
    
    
    
    
    
    
   