#battleship

#each grid will have following format :

#[y-coordinate, x-coordinate, Hit, ShipPiece]

#y-coordinate represents the letter of its y-position
#x-coordinate represents the digit of its x-position
#Hit will indicate if this box has been hit by the user during #that round.
#This will be 'False' by default in the beginning of each game.
#ShipPiece will be true if that box contains a ship piece, to #determine whether the user has hit it on target.
#These pieces will be randomly generated.

import random

def newGame():
    gameOver = False

    grids = [

                [
                    ['A', 1, False, False],
                    ['A', 2, False, False],
                    ['A', 3, False, False],
                    ['A', 4, False, False],
                    ['A', 5, False, False],
                ],

                [
                    ['B', 1, False, False],
                    ['B', 2, False, False],
                    ['B', 3, False, False],
                    ['B', 4, False, False],
                    ['B', 5, False, False],
                ],

                [
                    ['C', 1, False, False],
                    ['C', 2, False, False],
                    ['C', 3, False, False],
                    ['C', 4, False, False],
                    ['C', 5, False, False],
                ],

                [
                    ['D', 1, False, False],
                    ['D', 2, False, False],
                    ['D', 3, False, False],
                    ['D', 4, False, False],
                    ['D', 5, False, False],
                ],

                [
                    ['E', 1, False, False],
                    ['E', 2, False, False],
                    ['E', 3, False, False],
                    ['E', 4, False, False],
                    ['E', 5, False, False],
                ],

            ]

    for i in range(1, 6):
        shipXCoord = random.randrange(1, 6)
        shipYCoord = random.randrange(1, 6)

        grids[shipXCoord - 1][shipYCoord - 1][3] = True

    return grids, gameOver

def hitOrNot(grids, yPos, xPos):
    if grids[yPos - 1][xPos - 1][2] == False:
        printValue = '□'
    elif grids[yPos - 1][xPos - 1][2] == True and grids[yPos - 1][xPos - 1][3] == True:
        printValue = '#'
    else:
        printValue = 'X'
    return printValue
    

def description(grids):
    print( '\n' + "You have the current grids available for attack!: (□ = Available, X = Not Available, # = Ship)")
    
    print('\n'
          + '\t' + '1' + '\t' + '2' + '\t' + '3' + '\t' + '4' + '\t' + '5' '\n'
          + 'A' + '\t' + hitOrNot(grids,1,1) + '\t' + hitOrNot(grids,2,1) + '\t' + hitOrNot(grids,3,1) + '\t' + hitOrNot(grids,4,1) + '\t' + hitOrNot(grids,5,1) + '\n'
          + 'B' + '\t' + hitOrNot(grids,1,2) + '\t' + hitOrNot(grids,2,2) + '\t' + hitOrNot(grids,3,2) + '\t' + hitOrNot(grids,4,2) + '\t' + hitOrNot(grids,5,2) + '\n'
          + 'C' + '\t' + hitOrNot(grids,1,3) + '\t' + hitOrNot(grids,2,3) + '\t' + hitOrNot(grids,3,3) + '\t' + hitOrNot(grids,4,3) + '\t' + hitOrNot(grids,5,3) + '\n'
          + 'D' + '\t' + hitOrNot(grids,1,4) + '\t' + hitOrNot(grids,2,4) + '\t' + hitOrNot(grids,3,4) + '\t' + hitOrNot(grids,4,4) + '\t' + hitOrNot(grids,5,4) + '\n'
          + 'E' + '\t' + hitOrNot(grids,1,5) + '\t' + hitOrNot(grids,2,5) + '\t' + hitOrNot(grids,3,5) + '\t' + hitOrNot(grids,4,5) + '\t' + hitOrNot(grids,5,5))


def userDecision(grids):
    hitCount = 0

    userInput = input("Input grid value (Letter then Number): ")

    if userInput[0].upper() == 'A':
        userXCoord = 1
    elif userInput[0].upper() == 'B':
        userXCoord = 2
    elif userInput[0].upper() == 'C':
        userXCoord = 3
    elif userInput[0].upper() == 'D':
        userXCoord = 4
    else:
        userXCoord = 5

    grids[int(userInput[1]) - 1][userXCoord - 1][2] = True

    if grids[int(userInput[1]) - 1][userXCoord - 1][3] == True:
        result = "\nYou have hit one of the enemy ship pieces. You watch it drown into the deep ocean ever so slowly."
        grids[int(userInput[1]) - 1][userXCoord - 1][2] = True
        hitCount += 1
    else:
        result = "\nYou drop a missile into the sea to discover that no ship exists there."
        
    return result, hitCount


def main():
    grids, gameOver = newGame()
    gameCount = 0

    while gameOver == False:
        description(grids)
        result, hitCount = userDecision(grids)

        if hitCount == 1:
            gameCount += 1

        print('\n' + result)

        if gameCount == 5:
            gameOver = True

    print("Congratulations. You have won!")



main()
