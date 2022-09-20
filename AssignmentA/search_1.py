from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN
from itertools import chain
from copy import deepcopy

def check_neighbors(puzzle, front, s):
    zeroX, zeroY = puzzle.zero[0], puzzle.zero[1]

    
    if zeroX != puzzle.size-1:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX + 1, zeroY)
        newNode = Node(newPuzzle, puzzle, UP)

    if zeroY != 0:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX, zeroY-1)
        newNode = Node(newPuzzle, puzzle, RIGHT)
    if zeroX != 0:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX - 1, zeroY)
        newNode = Node(newPuzzle, puzzle, DOWN)
    if zeroY != puzzle.size-1:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX, zeroY+1)
        newNode = Node(newPuzzle, puzzle, LEFT)
    
    for i,y in front,s:
        if newNode.state.puzzle != i.state.puzzle and newNode.state.puzzle != y.state.puzzle:
            front.append(newNode)
    

    