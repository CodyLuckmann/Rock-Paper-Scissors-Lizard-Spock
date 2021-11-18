import time

class Player:
    def __init__(self, name):
        self.name = name
        
    gestures_list =["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    robolist = [1,2,3,4,5]
        
    def display_and_pick_gestures(self):
        gesture = int(input("\nPlease pick a gesture: \nRock = 1 \nPaper = 2 \nScissors = 3 \nLizard = 4 \nSpock = 5 \n\nChoice: "))
        result = gesture
        return result  
    
    def choose_game_mode(self):
        i =int(input("\nPlease press 1 for Single Player:  \nPlease press 2 for Multi-Player:\n "))
        if i == 1:
            return 1
        elif i == 2:
            return 2
        else:
            print('Invalid choice, enter again')
            

    