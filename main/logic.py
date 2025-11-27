import random
import os
picks = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}

class Game:

    def __init__(self):

        self.pointsP1 =  0
        self.pointsP2 =  0
        self.rounds = 0
        self.extended = False
        self.ongoing = False
        
def getRoundNumber():

    try:
        rounds = input("How many rounds do you want to play?\n")
        rounds = int(rounds)
    except:
        print("Invalid Input for number of rounds.")
        getRoundNumber()

    return rounds

def askExtended():

    try:
        extended = input("Do you want to play the extended game? (y/n)\n")
        if extended == "y" or extended == "n" :
            pass
        else:
            raise Exception()
    except:
        print("Invalid Input for number of rounds.")
        askExtended()

    if extended == "y":
        return True
    else:
        return False

def checkWinner(choice, enemyChoice, game):
    
    #converts int input to key pick value if not string
    if isinstance(choice, int):
        value = list(picks.keys())[choice-1]
    print("You picked " + value)
    print("The enemy picked " + enemyChoice)
    
    if value == enemyChoice:
        
        print("Draw!\n\n\n")
    elif enemyChoice in picks[value]:
        
        print("Win\n\n\n")
        game.pointsP1 += 1
    else:
        
        print("Lose!\n\n\n")
        game.pointsP2 += 1
        
    print("Score: " + str(game.pointsP1) + " : " + str(game.pointsP2) + "\n")


def playNormal(game):

    choice = input("Whats your move?\nRock (1)\nPaper (2)\nScissors (3)\n")

    try:
        if (int(choice) > 0 and int(choice) < 4):
            enemyChoice = list(picks.keys())[random.randint(0,2)]
            checkWinner(int(choice), enemyChoice, game)
        else:
            print("Invalid input")
            raise Exception()
    except:
        if(choice.lower() == "rock" or choice.lower() == "paper" or choice.lower() == "scissors"):
            checkWinner(choice, enemyChoice, game)
        else:
            print("Invalid input\n\n")
            playNormal(game)
            
def playExtended(game):

    choice = input("Whats your move?\nRock (1)\nPaper (2)\nScissors (3)\nLizard (4)\nSpock (5)")

    try:
        if (int(choice) > 0 and int(choice) < 6):
            enemyChoice = list(picks.keys())[random.randint(0,4)]
            checkWinner(int(choice), enemyChoice, game)
        else:
            print("Invalid input")
            raise Exception()
    except:
        if(choice.lower() == "rock" or choice.lower() == "paper" or choice.lower() == "scissors" or choice.lower() == "lizard" or choice.lower() == "spock"):
            checkWinner(choice, enemyChoice, game)
        else:
            print("Invalid input\n\n")
            playExtended(game)


def askAgain(game):
    try:
        value = input("Play again? (1)\nOr continue this match you sore loser (2)\nOr end? (3)")
        print(value)
        intValue = int(value)
        if intValue == 1 or intValue == 2:
            if intValue == 1:
                game.pointsP1 = 0
                game.pointsP2 = 0
                game.ongoing = False
            else:
                game.ongoing = True
            return True
        elif intValue == 3:
            return False
        else:
            raise Exception()
            
    except:
        #code stops when multiple wrong inputs and then right one?
        #still a problem
        askAgain(game)
    
def play(game):
    
    
    
    if not game.ongoing:
        game.extended = askExtended()
        
    game.rounds = getRoundNumber()
    
    os.system('clear')
    
    
    playedRounds = 0

    while playedRounds < game.rounds:
        if game.extended:
            playExtended(game)
        else:
            playNormal(game)
        

        playedRounds += 1
        pass

    
    if askAgain(game):
        play(game)
    else:
        pass


   


if __name__ == "__main__":
    
    game = Game()
    play(game)