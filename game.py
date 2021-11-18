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
                print('Player 1 wins') 
                sys.exit('')
            elif counterp2 == 2:
                print('Player 2 wins')
                sys.exit('')
            elif i == 1:
                x = Player.display_and_pick_gestures(x)
                while (x < 1) or (x > 5):
                    if (x < 1) or (x > 5):
                        print('Invalid choice, please choose again')
                        x = Player.display_and_pick_gestures(x)
                    else:
                        x = Player.display_and_pick_gestures(x)
                z = Robot.display_and_pick_gestures(Player.robolist)
            elif i == 2:
                print('\nPlayer one choose first\n')
                x = Player.display_and_pick_gestures(x)
                while (x < 1) or (x > 5):
                    if (x < 1) or (x > 5):
                        print('Invalid choice, please choose again')
                        x = Player.display_and_pick_gestures(x)
                    else:
                        x = Player.display_and_pick_gestures(x)
                print('\nPlayer two choose\n')
                z = Player.display_and_pick_gestures(z)
                while (z < 1) or (z > 5):
                    if (z < 1) or (z > 5):
                        print('Invalid choice, please choose again')
                        z = Player.display_and_pick_gestures(z)
                    else:
                        z = Player.display_and_pick_gestures(z)
                print('\nPlayer one and Player two chose\n')
                print(x)
                print(z)
            if ((x == 1) and ((z == 3) or (z == 4))):
                    counterp1 = counterp1 + 1
                    print("\nPlayer one wins this round\n")
            elif ((x == 2) and ((z == 1) or (z == 5))):
                    counterp1 = counterp1 + 1
                    print("\nPlayer one wins this round\n")
            elif ((x == 3) and ((z == 2) or (z == 4))):
                    counterp1 = counterp1 + 1
                    print("\nPlayer one wins this round\n")
            elif ((x == 4) and ((z == 5) or (z == 2))):
                    counterp1 = counterp1 + 1
                    print("\nPlayer one wins this round\n")
            elif ((x == 5) and ((z == 3) or (z == 1))):
                    counterp1 = counterp1 + 1
                    print("\nPlayer one wins this round\n")
            elif x == z:
                    print('\ntie\n')
            else:
                    counterp2 = counterp2 + 1
                    print("\nPlayer two wins this round\n")
            
            
            
    
        
    
    
    
    
    
    
    
   