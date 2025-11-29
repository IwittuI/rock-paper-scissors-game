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

#game obj to keep track of stats and options
class Game:
    def __init__(self):
        self.pointsP1 =  0
        self.pointsP2 =  0
        self.rounds = 0
        self.extended = False
        self.ongoing = False
        self.wins = 0
        self.losses = 0
        self.draws = 0
        
def getRoundNumber():
    try:
        rounds = int(input("\nHow many rounds do you want to play?\n"))

    except:
        print("Invalid Input for number of rounds.")
        return getRoundNumber()

    return rounds

def askExtended():
    extended = input("Do you want to play the extended game? (y/n)\n")
    
    match extended.lower():
        case "y" | "yes":
            return True
        case "n" | "no":
            return False
        case _:
            os.system('clear')
            print("Invalid Input for variant choice.")
            return askExtended()     

def checkWinner(choice, enemyChoice, game):
    #converts int input to key pick value if choice is not string
    if isinstance(choice, int):
        choice = list(picks.keys())[choice-1]
        
    os.system('clear')
    print("You picked " + choice)
    print("The enemy picked " + enemyChoice)
    
    #checks for draw first
    if choice == enemyChoice:
        print("Draw!\n")
        
    elif enemyChoice in picks[choice]: 
        print("Win\n")
        game.pointsP1 += 1
        
    else: 
        print("Lose!\n")
        game.pointsP2 += 1
     
    print("Score: " + str(game.pointsP1) + " : " + str(game.pointsP2) + "\n")


def playNormal(game):
    choice = input("Whats your move?\nRock (1)\nPaper (2)\nScissors (3)\n")
    #randomly picks the com choice from the list of keys (here for normal mode only the first 3)
    enemyChoice = list(picks.keys())[random.randint(0,2)]

    try:
        choice = int(choice)
        if choice > 0 and choice < 4:
            checkWinner(choice, enemyChoice, game)
            
        else:
            print("Invalid input")
            raise Exception()
        
    except:
        if(choice.lower() in list(picks.keys())[:3]):
            checkWinner(choice.lower(), enemyChoice, game)
            
        else:
            print("Invalid input\n\n")
            playNormal(game)
            
def playExtended(game):
    print("Whats your move?") 
    #loop through keys to make game expandable
    for i in range(0, len(picks)):
        print(list(picks.keys())[i].capitalize() + " (" +str(i + 1) + ")")
        
    choice = input()
    #randomly picks the com choice from the list of keys
    enemyChoice = list(picks.keys())[random.randint(0,4)]

    try:
        choice = int(choice)
        if choice > 0 and choice < 6:
            
            checkWinner(choice, enemyChoice, game)
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
    value = input("Play again? (1)\nOr continue this match you sore loser (2)\nOr go back to menu? (3)\n").lower()

    match value:
        #resets score for new game
        case "1" | "again":
            game.pointsP1 = 0
            game.pointsP2 = 0
            game.ongoing = False
            return True
        
        #only sets ongoing True so you dont get asked for extended again etc  
        case "2" | "continue":
            game.ongoing = True
            return True
        
        case "3" | "menu" | "end" | "exit":
            game.pointsP1 = 0
            game.pointsP2 = 0
            game.ongoing = False
            os.system('clear')
            return False
        
        case _:
            os.system('clear')
            print("Invalid input.")
            return askAgain(game)
        
def checkContinue(game):
    continueCheck = ""
    
    if not game.ongoing:
        if game.pointsP1 > game.rounds / 2 and game.rounds % 2 != 0 or game.pointsP1 >= game.rounds / 2 and game.rounds % 2 != 0:
            continueCheck = input("You technically already won do you want to continue? (y/n)\n")
            
        elif game.pointsP2 > game.rounds / 2 and game.rounds % 2 != 0 or game.pointsP2 >= game.rounds / 2 and game.rounds % 2 != 0:
            continueCheck = input("You technically already lost do you want to continue? (y/n)\n")
        
    if continueCheck != "":    
        match continueCheck.lower():
            case "":
                return True
            case "y" | "yes":
                game.ongoing = True
                return True
            case "n" | "no":
                return False
            case _:
                print("Invalid input.")
                return checkContinue(game)
    
    return True

def printWinner(game):
    match (game.pointsP1 > game.pointsP2):
        case True:
            print("You won!\n")
            game.wins += 1
            
        case False:
            if game.pointsP1 == game.pointsP2:
                print("Draw!\n")
                game.draws += 1
            else:
                print("You lost.\n")
                game.losses += 1      
               
        case _:
            print("Something went wrong")
        
def play(game):
    os.system('clear')
    #pre game
    #ask for variant if game is new
    if not game.ongoing:
        game.extended = askExtended()
    
    game.rounds = getRoundNumber()
    os.system('clear')
    
    #general game loop
    playedRounds = 0
    while playedRounds < game.rounds:
        if checkContinue(game):
            if game.extended:
                playExtended(game)
                
            else:
                playNormal(game)
        
        playedRounds += 1
    
    #post game
    printWinner(game)
    if askAgain(game):
        play(game)
        
def checkStats(game):
    os.system('clear')
    matches = game.wins + game.losses + game.draws
    print("You played a total of " + str(matches) + " matches!")
    print("You won a total of " + str(game.wins) + " times!")
    print("You lost a total of " + str(game.losses) + " times.\n")
    #do not display winrate if 0 wins
    try:
        print("That's a winrate of " + str(matches / game.wins) + "%!")
    except:
        pass
        
if __name__ == "__main__":
    game = Game()
    loop = True
    while loop:
        
        choice = input("What do you want to do?\nPlay (1)\nCheck Stats (2)\nEnd (3)\n").lower()
        match choice:
            case "1" | "play":
                play(game)
            case "2" | "stats" | "check stats" | "checkstats":
                checkStats(game)
            case "3" | "end":
                print("Bye!")
                loop = False