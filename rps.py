from random import randint
 
#list of player_input options
player_input = ["rock", "paper", "scissors"]
 
computer = player_input[randint(0,2)]
 
player = False
 
while player == False:
#set player to True
    player = raw_input("Choose either rock, paper, " +
                       "scissors. Press \'q\' to quit\n")
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
    elif choice == "q":
            exit()
    else:
        print("That's not an option you can play. Try again!")


    player = False
    computer = player_input[randint(0,2)]
