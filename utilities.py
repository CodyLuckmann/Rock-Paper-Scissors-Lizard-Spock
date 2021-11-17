class Utilites:
    
    gestures_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    
def display_welcome():
    print("Welcome to RPSLS!")    
    
def display_rules():   
    print("The rules are: \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock \nRock beats Lizard \nLizard beats Spock \nSpock beats Scissors \nScissors beats Lizard \nLizard beats Paper \nPaper beats Spock \nSpock beats Rock")


def choose_game_mode():
    int(input("For single player press: 1 \n For multiplayer press: 2 "))
    if input == 1:
        return 1
    else:
        return 2
    
def user_name():
    Player_one = input("Please enter your name: ")
    return input

def display_game_winner():
    print('Wins!!')

    


