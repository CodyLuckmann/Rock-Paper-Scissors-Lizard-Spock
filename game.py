from player import Player
from utilities import Utilites
from robot import Robot
import sys

class Game:
    def __init__(self):
        pass
    
    Utilites.display_welcome()
    Utilites.display_rules()
    
    # game function (runs both Single & Multi game)
    def game(i):
        x = 0
        z = 0
        counterp1 = 0
        counterp2 = 0
        # Starts game in Multi-player mode
        while (counterp1 < 2) or (counterp2 < 2):
            # Announce Player 1 wins and ends game
            if counterp1 == 2:
                sys.exit("Player one wins the game!")
            # Announce Player 2 wins game and ends game
            elif counterp2 == 2:
                sys.exit("Player two wins the game!") 
            # Displays gesture options
            elif i == 1:
                x = Player.display_and_pick_gestures(x)
                while (x < 1) or (x > 5):
                    # Prompted when invalid input is enter (ie. out of range) also re-displays gesture options
                    if (x < 1) or (x > 5):
                        print('Invalid choice, please choose again')
                        x = Player.display_and_pick_gestures(x)
                    else:
                        # Fail safe 
                        x = Player.display_and_pick_gestures(x)
                # Accessing random Robot options
                z = Robot.display_and_pick_gestures(Player.robolist)
            # Starts game in Single-player
            elif i == 2:
                print('\nPlayer one choose first\n')
                x = Player.display_and_pick_gestures(x)
                # Prompted when invalid input is enter (ie. out of range) also re-displays gesture options
                while (x < 1) or (x > 5):
                    if (x < 1) or (x > 5):
                        print('Invalid choice, please choose again')
                        x = Player.display_and_pick_gestures(x)
                    # Displays gesture options
                    else:
                        x = Player.display_and_pick_gestures(x)
                print('\nPlayer two choose\n')
                 # Accessing Player input options
                z = Player.display_and_pick_gestures(z)
                while (z < 1) or (z > 5):
                    if (z < 1) or (z > 5):
                        print('Invalid choice, please choose again')
                        z = Player.display_and_pick_gestures(z) 
                    else:
                        # Fail safe
                        z = Player.display_and_pick_gestures(z)
                # Print choices for both players
                print('\nPlayer one and Player two chose\n')
                print(x)
                print(z)
            # Print Player one winner based on gesture pick combination
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
            # Prints "Tie" messsage to the console 
            elif x == z:
                    print('\ntie\n')
            # Prints two winner based on gesture pick combination 
            else:
                    counterp2 = counterp2 + 1
                    print("\nPlayer two wins this round\n")
    
            
            
    
        
    
    
    
    
    
    
    
   