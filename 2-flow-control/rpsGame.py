import sys, random

print('ROCK','PAPER',"SCISSORS")

#keep track of variables
wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %sLoss , %sTies" %(wins, losses, ties))
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        playerMove = input()
        if playerMove == 'q':
            sys.exit() #Quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break #Break out of the player input loop.
        print("Type one of r, p, s or q")
    
    #Display what player choose
    if playerMove == "r":
        print("ROCK versus ...")
    elif playerMove == "p":
        print("PAPER versus ...")
    elif playerMove == "s":
        print("SCISSORS versus ...")
    
    #Display what computer choose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = "r"
        print("ROCK")
    elif randomNumber == 2:
        computerMove = "p"
        print("PAPER")
    elif randomNumber == 3:
        computerMove == "s"
        print("SCISSORS")
    
    #Display and record the win/lose/tie
    if playerMove == computerMove:
        print("It is a tie")
        ties += 1
    elif playerMove == "r" and computerMove == "s":
        print("You win!")
        wins += 1
    elif playerMove == "p" and computerMove == "r":
        print("You win!")
        wins += 1
    elif playerMove == "s" and computerMove == "p":
        print("You win!")
        wins += 1
    elif playerMove == "r" and computerMove == "p":
        print("You lose!")
        losses += 1
    elif playerMove == "p" and computerMove == "s":
        print("You lose!")
        losses += 1
    elif playerMove == "s" and computerMove == "r":
        print("You lose!")
        losses += 1
