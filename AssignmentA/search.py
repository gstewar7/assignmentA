from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN
from copy import deepcopy


def check_neighbors(node):
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
        print("Puzzle too big, did not try")
        return states_searched, final_solution
        
    frontier = [Node(puzzle)]
    #current = frontier [0]

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
            # #print(current.state.print_puzzle())
            # print("Depth level", current.depth)
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

    states_searched = []
    final_solution = []

    # TODO: WRITE CODE
    if puzzle.size > 3:
        print("Puzzle too big, did not try")
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
            # print(current.state.print_puzzle())
            # print("Depth level", current.depth)
            return states_searched, final_solution
        elif current.depth > 17:
            continue

        newNodes = check_neighbors(current)
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
            # print(current.state.print_puzzle())
            # print("Depth level", current.depth)
            return states_searched, final_solution
        
        newNodes = check_neighbors(current)
        for i in newNodes:
            if i.state.puzzle not in frontier_puzzles and i.state.puzzle not in explored_puzzles:
                frontier.append(i)
                frontier_puzzles.append(i.state.puzzle)
        print("a")
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
    # def solution(size):
    #     puzzle = [[(j*size)+i+1 for i in range(size)] for j in range(size)]
    #     puzzle[size-1][size-1] = 0
    solution = NPuzzle(puzzle.size)

    def heuristic_a2(puzzle, solution):
        def index_2d(lis, v):
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

    #heur = heuristic_a2(puzzle.puzzle, solution)
    ##################################################
    ##################################################
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
            # print(current.state.print_puzzle())
            # print("Depth level", current.depth)
            return states_searched, final_solution
        
        newNodes = check_neighbors(current)
        for i in newNodes:
            if i.state.puzzle not in frontier_puzzles and i.state.puzzle not in explored_puzzles:
                frontier.append(i)
                frontier_puzzles.append(i.state.puzzle)
        
        frontier.sort(key=lambda x: x.depth+heuristic_a2(x.state.puzzle, solution))

    return states_searched, final_solution