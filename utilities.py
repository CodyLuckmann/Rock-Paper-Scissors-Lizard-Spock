
class Utilites:
    
    
    
    
    
    def display_welcome():
        print("\n\nWelcome to RPSLS!\n")    
        
    def display_rules():   
        print("The rules are: \nRock beats Scissors \nScissors beats Paper \nPaper beats Rock \nRock beats Lizard \nLizard beats Spock \nSpock beats Scissors \nScissors beats Lizard \nLizard beats Paper \nPaper beats Spock \nSpock beats Rock\n")

    def choose_game_mode():
        i = 0
        while i != (1 or 2):
            i = int(input("\nPress 1 for single player:  \nPress 2 for Multi-Player:\n "))
            # print(i)
            if i == 1:
                return 1
            elif i == 2:
                return 2
            else:
                print('Invalid choice, enter again')



    


