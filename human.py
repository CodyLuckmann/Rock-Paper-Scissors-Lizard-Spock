from utilities import Utilites
from player import Player 

class Human(Player):
    def __init__(self, name):
        self.name = name 
        pass
    
    def display_and_pick_gestures(self):
    