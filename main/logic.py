import random
import os
#dict of possible picks | values are the winning matchups
picks = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"],
}

#game obj to keep track of scores rounds and what type
class Game:
    def __init__(self):
        self.pointsP1 =  0
        self.pointsP2 =  0
        self.rounds = 0
        self.extended = False
        self.ongoing = False
        
def getRoundNumber():

    try:
        rounds = int(input("How many rounds do you want to play?\n"))

    except:
        print("Invalid Input for number of rounds.")
        return getRoundNumber()

    return rounds

def askExtended():

    try:
        extended = input("Do you want to play the extended game? (y/n)\n")
        if extended == "y":
            return True
        elif extended == "n":
            return False
        else:
            raise Exception()
    except:
        print("Invalid Input for number of rounds.")
        return askExtended()

def checkWinner(choice, enemyChoice, game):
    
    #converts int input to key pick value if not string
    if isinstance(choice, int):
        choice = list(picks.keys())[choice-1]
    print("You picked " + choice)
    print("The enemy picked " + enemyChoice)
    
    #checs for draw first
    if choice == enemyChoice:
        
        print("Draw!\n\n\n")
    elif enemyChoice in picks[choice]:
        
        print("Win\n\n\n")
        game.pointsP1 += 1
    else:
        
        print("Lose!\n\n\n")
        game.pointsP2 += 1
     
    print("Score: " + str(game.pointsP1) + " : " + str(game.pointsP2) + "\n")


def playNormal(game):

    choice = input("Whats your move?\nRock (1)\nPaper (2)\nScissors (3)\n")
    enemyChoice = list(picks.keys())[random.randint(0,2)]

    try:
        if (int(choice) > 0 and int(choice) < 4):
            
            checkWinner(int(choice), enemyChoice, game)
            
        else:
            print("Invalid input")
            raise Exception()
        
    except:
        if(choice.lower() in list(picks.keys())[:2]):
            checkWinner(choice, enemyChoice, game)
            
        else:
            print("Invalid input\n\n")
            playNormal(game)
            
def playExtended(game):

    print("Whats your move?")
    
    #loop through keys to make game expandable
    for i in range(0, len(picks)):
        print(list(picks.keys())[i].capitalize() + " (" +str(i + 1) + ")")
    choice = input()
    
    enemyChoice = list(picks.keys())[random.randint(0,4)]

    try:
        if (int(choice) > 0 and int(choice) < 6):
            
            checkWinner(int(choice), enemyChoice, game)
        else:
            print("Invalid input")
            raise Exception()
    except:
        if(choice.lower() in list(picks.keys())):
            checkWinner(choice, enemyChoice, game)
        else:
            print("Invalid input\n\n")
            playExtended(game)


def askAgain(game):
    try:
        value = int(input("Play again? (1)\nOr continue this match you sore loser (2)\nOr end? (3)\n"))

        if value == 1 or value == 2:
            #resets score for new game
            if value == 1:
                game.pointsP1 = 0
                game.pointsP2 = 0
                game.ongoing = False
            #only sets ongoing True so you dont get asked for extended again   
            else:
                game.ongoing = True
                
            return True
        
        elif value == 3:
            return False
        else:
            raise Exception()
            
    except:
        return askAgain(game)
    
def play(game):
    
    #asked for variant if game is new
    if not game.ongoing:
        game.extended = askExtended()
        
    game.rounds = getRoundNumber()
    os.system('clear')
    
    #general game loop
    playedRounds = 0
    while playedRounds < game.rounds:
        if game.extended:
            playExtended(game)
            
        else:
            playNormal(game)
        
        playedRounds += 1
        
    if askAgain(game):
        play(game)
    
if __name__ == "__main__":
    game = Game()
    play(game)