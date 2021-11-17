
#from utilities import Utilites
#from robot import Robot
#from human import Human


class Player:
    def __init__(self, name):
        self.name = name
        
    gestures_list =["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        
    def display_and_pick_gestures(self):
        gesture = int(input('Please pick a gesture: \nrock = 1 \n paper = 2 \n scissors = 3 \n lizard = 4 \n spock = 5'))
        return gesture
    
           
    def user_name(self):
        player_input = input("Please enter your name: ")
        result = player_input
        return result
    
    def choose_game_mode(self):
        i =int(input("\nPlease press 1 for Single Player:  \nPlease press 2 for Multi-Player: "))
        if i == 1:
            return 1
        elif i == 2:
            return 2
        else:
            print('Invalid choice, enter again')
            

    