from random import randint
 
#list of player_input options
player_input = ["rock", "paper", "scissors"]
 
computer = player_input[randint(0,2)]
 
player = False
 
while player == False:
#set player to True
    player = input("Choose either rock, paper, scissors? Or press 'q' to quit")
    if player == computer:
        print("Tie!, try again!")
    elif player == "rock":
        if computer == "paper":
            print("You lose! You get nothing!")
        else:
            print("Yay! You win!")
    elif player == "paper":
        if computer == "scissors":
            print("You lose! You get nothing!")
        else:
            print("Yay! You win!")
    elif player == "scissors":
        if computer == "rock":
            print("You lose. You get nothing!")
        else:
            print("You win!")
    else:
        print("That's not an option you can play. Try again!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = player_input[randint(0,2)]
