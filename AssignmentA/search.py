from asyncio import start_server
from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN
from itertools import chain
from copy import deepcopy

def check_last_move(target, prevMoves):
    if len(prevMoves) > 0:
        if target == prevMoves[-1]:
            return True
    return False

def check_neighbors(node):
    puzzle = node.state
    zeroX, zeroY = puzzle.zero[0], puzzle.zero[1]
    newNodes = []
    
    if zeroX != puzzle.size-1:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX + 1, zeroY)
        newNodes.append(Node(newPuzzle, node, UP))

    if zeroY != 0:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX, zeroY-1)
        newNodes.append(Node(newPuzzle, node, RIGHT))
    if zeroX != 0:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX - 1, zeroY)
        newNodes.append(Node(newPuzzle, node, DOWN))
    if zeroY != puzzle.size-1:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX, zeroY+1)
        newNodes.append(Node(newPuzzle, node, LEFT))
    
    return newNodes


def BFS(puzzle):
    """
    Breadth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """


    states_searched = [Node(puzzle)]
    final_solution = []
    
    
    # TODO: WRITE CODE
    if puzzle.size > 3:
        print("Puzzle too big, did not try")
        return states_searched, final_solution
    frontier = [Node(puzzle)]
    current = frontier [0]
    while len(frontier):
        

        current = frontier.pop(0)
        states_searched.append(current)


        if current.state.check_puzzle():          
            final_solution = current.moves
            print(current.state.print_puzzle())
            print("Depth level", current.depth)
            return states_searched, final_solution
        else:
            newNodes = check_neighbors(current)
            for i in newNodes:

                """ for j in states_searched:
                    if i.state.puzzle == j.state.puzzle and len(newNodes) > 0:
                        newNodes.pop(0)
                for j in frontier:
                    if i.state.puzzle == j.state.puzzle and len(newNodes) > 0:
                        newNodes.pop(0) """
                if i.parent.moves == []:
                    frontier.append(i)
                    continue
                elif i.moves != []:
                    if abs(i.parent.moves[-1] - i.moves[-1]) != 2: 
                        frontier.append(i)

    #end of while loop

    print("Depth limit reached")
    return states_searched, final_solution

def DFS(puzzle):
    """
    Depth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []

    # TODO: WRITE CODE



    return states_searched, final_solution


def A_Star_H1(puzzle):
    """
    A-Star with Heuristic 1

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []

    # TODO: WRITE CODE

    return states_searched, final_solution


def A_Star_H2(puzzle):
    """
    A-Star with Heauristic 2

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []

    # TODO: WRITE CODE

    return states_searched, final_solution