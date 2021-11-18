from utilities import Utilites
import random


class Test:
    z = 0


    def player_choice(self, p2c=None):
        #Utilites.display_welcome()
        player1_choice = 0
        player2_choice = 0
        if (player1_choice == 1 and player2_choice == 3 or 4):
            player1_choice = True
        elif (player1_choice == 2 and player2_choice == 1 or 5):
            player1_choice = True
        elif (player1_choice == 3 and player2_choice == 2 or 4):
            player1_choice = True
        elif (player1_choice == 4 and player2_choice == 5 or 2):
            player1_choice = True
        elif (player1_choice == 5 and player2_choice == 3 or 1):
            player1_choice = True
        elif player1_choice == player2_choice:
            print('tie')
            #need to ask the user input again
        else:
            player1_choice = False
        
test = Test()
test.player_choice()
