from robot import Robot

class Utilites:
    
    gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
    def display_welcome():
        print("\n\nWelcome to RPSLS!\n")    
        
    def display_rules():   
        print("The rules are: \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock \nRock beats Lizard \nLizard beats Spock \nSpock beats Scissors \nScissors beats Lizard \nLizard beats Paper \nPaper beats Spock \nSpock beats Rock\n")


    def choose_game_mode():
        int(input("\nFor single player press: 1  \nFor multiplayer press: 2 "))
        if input == 1:
            return 1
        else:
            return 2
        
    def choose_player2_mode():
        player1 = "X"
        i = int(input("Please press Y to play against a AI or Z to play against Human. ") 
        if i == "Y"
        # then robot 
        # player2 = AI 
        # set random
        if i == "Z"
        # player2 = Human
        # alternate plays 
        
        
    def user_name():
        Player_one = input("Please enter your name: ")
        return input

    def display_game_winner():
        print('Wins!!')

    


