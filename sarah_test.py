# Game Tuple Example

# Human vs. AI
gesture_wins = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"), ("rock", "lizard"), ("lizard", "spock"), 
                ("spock", "scissors"), ("scissors", "lizard"), ("lizard", "paper"), ("paper", "spock"), ("spock", "rock")] 
turns = [gesture[1] for gesture in gesture_wins]  

player1_score, player2_score = (0, 0) 
player = input("Enter rock / paper / scissors / lizard / spock / quit: ")
while player1 != "quit":
    player2 = random.choice(turns)
    print("You chose {}, Player2 chose {}") 
    if player1 == player2:
        print("It's a Tie!")
    elif (player1, player2) in turns:
        print("You Win!")
        player1_score += 1
    elif (player2, player1) in turns:
        print("Player2 Wins!")
        player2_score += 1
    else: 
        print("Invalid Entry. Please re-enter move.") 
        print("Hint: Please check spelling, and use all lower case. ")         
        player = input("Enter rock / paper / scissors / lizard / spock / quit: ")

print("Final Score") 
print("You're score is {}, Player2's score is {}. ") # {player1_score}, {player2_score} 
print("The final winner is {winner}.")
