from player import Player 
from human import Human 
from robot import Robot 
import random
# Game Tuple Example 

human_score = 0
robot_score = 0

class Game_2:
    def __init__(self):
        self.player = Player()
        self.human = Human()
        self.robot = Robot()

    def run_game_2(self, human_score, robot_score):
        # Human vs. AI
        gesture_choice = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"), ("rock", "lizard"), ("lizard", "spock"), ("spock", "scissors"), ("scissors", "lizard"), ("lizard", "paper"), ("paper", "spock"), ("spock", "rock")] 
        
        turns = [gesture[1] for gesture in gesture_choice]  
        # print(turns)

        human = input("Enter rock / paper / scissors / lizard / spock: ") # quit >2 option
        robot = random.choice(turns)
        
        human_score, robot_score = (0, 0)
               
        if human != "quit":
            robot = random.choice(turns)
            print("You chose {}, Player2 chose {}") 
            
        elif human == robot:
            print("Sorry, it's a Tie!")
                
        elif (human, robot) in turns:
            print("You Won!")
            human_score += 1
                
        elif (robot, human) in turns:
            print("Player2 Wins!")
            robot_score += 1
        # else
            #     end loop player >2 points 
            #     print("Invalid Entry. Please re-enter move.") 
            #     print("Hint: Please check spelling, and use all lower case. ")         
            #     Human = input("Enter rock / paper / scissors / lizard / spock / quit: ")

        print("Final Score") 
        print("You're score is {}, Robot's score is {}. ") # {Human_score}, {Robot_score} 
        print("The final winner is {winner}.")


x = 0  
Game_2.run_game_2(x, human_score, robot_score) 
