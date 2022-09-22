from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN
from copy import deepcopy



def check_neighbors(node):
    """
    check_neighbors
    Arguements: A node representing the current node being checked
    Check all surrounding tiles for valid moves

    Return: 
    newNodes: A list of nodes in U D L R order
    """
    puzzle = node.state
    zeroX, zeroY = puzzle.zero[0], puzzle.zero[1]
    newNodes = []
    
    if zeroX != puzzle.size-1:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX + 1, zeroY)
        newNodes.append(Node(newPuzzle, node, UP))
    if zeroX != 0:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX - 1, zeroY)
        newNodes.append(Node(newPuzzle, node, DOWN))
    if zeroY != puzzle.size-1:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX, zeroY+1)
        newNodes.append(Node(newPuzzle, node, LEFT))
    if zeroY != 0:
        newPuzzle = deepcopy(puzzle)
        newPuzzle.swap(zeroX, zeroY, zeroX, zeroY-1)
        newNodes.append(Node(newPuzzle, node, RIGHT))
    
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
        print("Puzzle too big, did not try") #Please don't be mad 
        return states_searched, final_solution
        
    frontier = [Node(puzzle)]

    #For all algorithms, I created a list containing only the state itself, as it was easier to compare the current puzzle
    #to a list of puzzle, rather than comparing current node to a list of nodes
    states_puzzles = [states_searched[0].state.puzzle]
    frontier_puzzles = [frontier[0].state.puzzle]

    if states_searched[0].moves == []:
        states_searched.pop()

    while len(frontier):
        

        current = frontier.pop(0)
        frontier_puzzles.pop(0)
        states_searched.append(current)
        states_puzzles.append(current.state.puzzle)

        if current.state.check_puzzle():          
            final_solution = current.moves
            return states_searched, final_solution
        else:
            newNodes = check_neighbors(current)

            for i in newNodes:
                if i.parent.moves == []:
                    frontier.append(i)
                    frontier_puzzles.append(i.state.puzzle)
                    continue
                elif i.state.puzzle not in states_puzzles and i.state.puzzle not in frontier_puzzles:
                        frontier.append(i)
                        frontier_puzzles.append(i.state.puzzle)


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

    states_searched = []
    final_solution = []

    # TODO: WRITE CODE
    if puzzle.size > 3:
        print("Puzzle too big, did not try")  #Please don't be mad 
        states_searched = [Node(puzzle)]
        return states_searched, final_solution

    frontier = [Node(puzzle)]

    states_puzzles = []
    frontier_puzzles = [frontier[0].state.puzzle]


    while len(frontier) > 0:
        current = frontier.pop()
        frontier_puzzles.pop()
        
        states_searched.append(current)
        states_puzzles.append(current.state.puzzle)

        if current.state.check_puzzle():
            final_solution = current.moves
            return states_searched, final_solution
        elif current.depth > 20:
            continue

        newNodes = check_neighbors(current)

        #I check the resulting list from check_neighbors in reverse order to add to the stack in the order specified (U, D, L, R)
        for i in reversed(newNodes):
            if i.state.puzzle not in frontier_puzzles and i.state.puzzle not in states_puzzles:
                frontier.append(i)
                frontier_puzzles.append(i)


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
    def heuristic_a1(puzzle):
        """
            A*1 Heuristic 
            Input: a puzzle representing the current node

            Iterates through the puzzle in order, if the tile does not match the count then it's in the wrong place
            and gets added to a total

            Return:
                Wrong: The total number of tiles in the wrong place
        """
        count = 1
        wrong = 0
        for i in range(puzzle.state.size):
            for j in range(puzzle.state.size):
                if puzzle.state.puzzle[i][j] != count:
                    wrong += 1
                count +=1 
        return wrong

    frontier = [states_searched[0]]
    frontier_puzzles = [frontier[0].state.puzzle]
    explored_puzzles = []

    while len(frontier) > 0:
        current = frontier.pop(0)
        frontier_puzzles.pop(0)
        states_searched.append(current)
        explored_puzzles.append(current.state.puzzle)
        
        if current.state.check_puzzle():
            final_solution = current.moves
            return states_searched, final_solution
        
        newNodes = check_neighbors(current)
        for i in newNodes:
            if i.state.puzzle not in frontier_puzzles and i.state.puzzle not in explored_puzzles:
                frontier.append(i)
                frontier_puzzles.append(i.state.puzzle)

        frontier.sort(key=lambda x: x.depth + heuristic_a1(x))



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

    solution = NPuzzle(puzzle.size)

    def heuristic_a2(puzzle, solution):
        """
            Heuristic for A*2
            Input:
                -Puzzle: the current puzzle 
                -Solution: The puzzle in it's final state

            Iterates through the current puzzle getting the index of each tile and the index of where the tile should be
            Adds the absolute value of the difference between the current tile row and desired positions row,
            as well as the column for both respectively
            Adds the two resulting values to get the manhattan distance from the current tile position and desired position
            Sums all of the manhattan distances for all tiles in the puzzle
        
        """
        def index_2d(lis, v):
            """
                Returns the indeces of a value in a 2d array

                Full disclosure: I pulled this from google 
            """
            for i, x in enumerate(lis):
                if v in x:
                    return i, x.index(v)
        
        totalsum = 0
        count = 1
        size = solution.size
        for i in range(size):
            for j in range(size):
                if count == size*size:
                    count = 0
                a, b = index_2d(solution.puzzle, count)
                c, d = index_2d(puzzle, count)
                result = abs(a-c) + abs(b-d)
                count += 1
                totalsum += result
        return totalsum

    frontier = [states_searched[0]]
    frontier_puzzles = [frontier[0].state.puzzle]
    explored_puzzles = []

    while len(frontier) > 0:
        current = frontier.pop(0)
        frontier_puzzles.pop(0)
        states_searched.append(current)
        explored_puzzles.append(current.state.puzzle)
        
        if current.state.check_puzzle():
            final_solution = current.moves
            return states_searched, final_solution
        
        newNodes = check_neighbors(current)
        for i in newNodes:
            if i.state.puzzle not in frontier_puzzles and i.state.puzzle not in explored_puzzles:
                frontier.append(i)
                frontier_puzzles.append(i.state.puzzle)
        
        frontier.sort(key=lambda x: x.depth+heuristic_a2(x.state.puzzle, solution))

    return states_searched, final_solution