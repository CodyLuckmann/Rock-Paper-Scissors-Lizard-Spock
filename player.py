
from utilities import Utilites
from robot import Robot
from human import Human


class Player:
    def __init__(self, name=None):
        self.name = name
        
        _gestures_list =["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        
    def display_and_pick_gestures(self):
        gesture = int(input('Please pick a gesture: \nrock = 1 \n paper = 2 \n scissors = 3 \n lizard = 4 \n spock = 5'))
        return gesture

    