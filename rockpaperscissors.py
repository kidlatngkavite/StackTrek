# player 1 input
# player 2 input
# output win lose draw



player1 = input("Input Player 1:")
player2 = input("Input Player 1:")

#if player1 == player2 : 
#        print(f"Draw")
if player1 == "rock" : 
    if player2 == "rock" : 
        print(f"Player 2 Wins")
    elif player2 == "paper" : 
        print(f"Player 1 Wins")
    elif player2 == "scissors" : 
        print(f"Player 1 Wins")
              
elif player1 == "paper" : 
    if player2 == "rock" : 
        print(f"Player 2 Wins")
    elif player2 == "paper" : 
        print(f"Player 1 Wins")
    elif player2 == "scissors" : 
        print(f"Player 1 Wins")
        
elif player1 == "paper" : 
    if player2 == "rock" : 
        print(f"Player 2 Wins")
    elif player2 == "paper" : 
        print(f"Player 1 Wins")
    elif player2 == "scissors" : 
        print(f"Player 1 Wins")