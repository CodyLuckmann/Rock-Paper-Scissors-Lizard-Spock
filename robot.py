import random
from player import Player

class Robot(Player):
    def __init__(self):
        self.processor = "Quad 186"#

    def display_and_pick_gestures(list):
        ran1 = random.choice(Player.robolist)
        print(f'Robot choice: {ran1}')
        result = ran1
        return result
