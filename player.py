
from utilities import Utilites
from robot import Robot
from human import Human

gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]


class Player:
    def __init__(self, name):
    # name
        self.name = name
        
        
    def display_and_pick_gestures(self):
        gesture = int(input('rock = 1 \n paper = 2 \n scissors = 3 \n lizard = 4 \n spock = 5'))
        return gesture
        
    # method - pick/choose gesture
    
    
    # human(self, pick)
    
    # AI
    