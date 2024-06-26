# Play command line Rock-Paper-Scissors
# By: Mattheu Jimenez

import random

possibleChoices = ["Rock", "Paper", "Scissors"]
playerPoints = 0
computerPoints = 0
isTwo = False

while isTwo == False:
    playerChoice = str.capitalize(input("Rock, paper, scissors... SHOOT! "))
    computerChoice = possibleChoices[random.randint(0,2)]

    print(f"The computer picks {computerChoice}")

    if playerChoice != possibleChoices[0] and playerChoice != possibleChoices[1] and playerChoice != possibleChoices[2]:
       print("Please enter rock, paper, or scissors. (Check your spelling and no spaces.)")
    elif computerChoice == "Rock" and playerChoice == "Rock":
         print("Draw! No one gets a point.")
    elif computerChoice == "Rock" and playerChoice == "Paper":
       print("Player wins! You get a point.")
       playerPoints = playerPoints + 1
    elif computerChoice == "Rock" and playerChoice == "Scissors":
        print("Computer wins! The computer gets get a point.")
        computerPoints = computerPoints + 1
    elif computerChoice == "Paper" and playerChoice == "Paper":
        print("Draw! No one gets a point.")
    elif computerChoice == "Paper" and playerChoice == "Scissors":
        print("Player wins! You get a point.")
        playerPoints = playerPoints + 1
    elif computerChoice == "Paper" and playerChoice == "Rock":
        print("Computer wins! The computer gets a point.")
        computerPoints = computerPoints + 1
    elif computerChoice == "Scissors" and playerChoice == "Scissors":
        print("Draw! No one gets a point.")
    elif computerChoice == "Scissors" and playerChoice == "Rock":
         print("Player Wins! You get a point.")
         playerPoints = playerPoints + 1
    elif computerChoice == "Scissors" and playerChoice == "Paper":
          print("Computer Wins! The computer gets a point.")
          computerPoints = computerPoints + 1


    print(f"The socre is {playerPoints} - {computerPoints}")

    if playerPoints == 2:
        isTwo = True
        print("The game is over, the player won!")
    elif computerPoints == 2:
        isTwo = True
        print("The game is over, the computer won!")


    

  

