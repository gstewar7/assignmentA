from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN
from copy import deepcopy

def check_last_move(target, prevMoves):
    if len(prevMoves) > 0:
        if target == prevMoves[-1]:
            return True
    return False

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
    queue = [Node(puzzle)]
    parentNode = Node(puzzle)

    while len(queue) != 0:
        popped = queue.pop(0)        
        
        states_searched.append(popped)
        #print(popped.print_puzzle())        
        zeroX = popped.state.zero[0]
        zeroY = popped.state.zero[1]

        if popped.state.check_puzzle():
            print(popped.print_puzzle())
            popped.moves = [popped.moves[len(popped.moves) - i]
                for i in range(1, len(popped.moves)+1)]
                
            final_solution = popped.moves
            return states_searched, final_solution
        else:
                
            if zeroY != 0 and not check_last_move(UP, popped.moves) :
                newPuzzle = deepcopy(popped.state)
                newPuzzle.swap(zeroX, zeroY, zeroX, zeroY-1)
                newNode = Node(newPuzzle, popped, DOWN)
                queue.append(newNode)

            if zeroX != puzzle.size-1 and not check_last_move(RIGHT, popped.moves)  :
                newPuzzle = deepcopy(popped.state)
                newPuzzle.swap(zeroX, zeroY, zeroX+1, zeroY)
                newNode = Node(newPuzzle, popped, LEFT)
                queue.append(newNode)

            if zeroY != puzzle.size-1 and not check_last_move(DOWN, popped.moves) :
                newPuzzle = deepcopy(popped.state)
                newPuzzle.swap(zeroX, zeroY, zeroX, zeroY+1)
                newNode = Node(newPuzzle, popped, UP)
                queue.append(newNode)

            if zeroX != 0 and not check_last_move(LEFT, popped.moves) :
                newPuzzle = deepcopy(popped.state)
                newPuzzle.swap(zeroX, zeroY, zeroX-1, zeroY)
                newNode = Node(newPuzzle, popped, RIGHT)
                queue.append(newNode)







    
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
    states_searched = [Node(puzzle)]
    final_solution = []
    # TODO: WRITE CODE
    queue = [Node(puzzle)]
    parentNode = Node(puzzle)
    popped = Node(puzzle)

    while len(queue) != 0 and popped.depth < 25:
        popped = queue.pop(0)        
        
        states_searched.append(popped)
        #print(popped.print_puzzle())        
        zeroX = popped.state.zero[0]
        zeroY = popped.state.zero[1]

        if popped.state.check_puzzle():
            print(popped.print_puzzle())
            popped.moves = [popped.moves[len(popped.moves) - i]
                for i in range(1, len(popped.moves)+1)]
                
            final_solution = popped.moves
            return states_searched, final_solution
        else:
                
            if zeroY != 0 and not check_last_move(UP, popped.moves) :
                newPuzzle = deepcopy(popped.state)
                newPuzzle.swap(zeroX, zeroY, zeroX, zeroY-1)
                newNode = Node(newPuzzle, popped, DOWN)
                queue.append(newNode)
                states_searched.append(newNode)
                continue

            if zeroX != puzzle.size-1 and not check_last_move(RIGHT, popped.moves)  :
                newPuzzle = deepcopy(popped.state)
                newPuzzle.swap(zeroX, zeroY, zeroX+1, zeroY)
                newNode = Node(newPuzzle, popped, LEFT)
                queue.append(newNode)                
                states_searched.append(newNode)
                continue

            if zeroY != puzzle.size-1 and not check_last_move(DOWN, popped.moves) :
                newPuzzle = deepcopy(popped.state)
                newPuzzle.swap(zeroX, zeroY, zeroX, zeroY+1)
                newNode = Node(newPuzzle, popped, UP)
                queue.append(newNode)
                states_searched.append(newNode)
                continue

            if zeroX != 0 and not check_last_move(LEFT, popped.moves) :
                newPuzzle = deepcopy(popped.state)
                newPuzzle.swap(zeroX, zeroY, zeroX-1, zeroY)
                newNode = Node(newPuzzle, popped, RIGHT)
                queue.append(newNode)
                states_searched.append(newNode)
                continue

    popped.moves = [popped.moves[len(popped.moves) - i]
                for i in range(1, len(popped.moves)+1)]
                
    final_solution = popped.moves
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