from helpers import NPuzzle, Node, UP, DOWN, LEFT, RIGHT
from search import BFS, DFS, A_Star_H1, A_Star_H2


def get_move_string(moves):
    """
    Helper function to print moves.

    """
    move_string = ""
    if len(moves) == 0:
        return "NONE"
    for move in moves:
        if move == UP:
            move_string = move_string + "U "
        elif move == LEFT:
            move_string = move_string + "L "
        elif move == DOWN:
            move_string = move_string + "D "
        elif move == RIGHT:
            move_string = move_string + "R "
        else:
            move_string = move_string + "INVALID "
    return move_string


def run_test(size, filename):
    """
    Takes a size and a filename,
    then creates a puzzle,
    reads it in from file,
    and runs each of the search algorithms

    """
    puzzle = NPuzzle(size)
    print(f"{filename}:")

    puzzle.read_puzzle(filename)
    states, moves = BFS(puzzle)
    if not states[-1].state.check_puzzle():
        print("    BFS | FAIL")
        print("          SOL MOVES: " + get_move_string(moves))
    else:
        print("    BFS | PASS")
        print("          SOL MOVES: " + get_move_string(moves))

    puzzle.read_puzzle(filename)
    states, moves = DFS(puzzle)
    if not states[-1].state.check_puzzle():
        print("    DFS | FAIL")
        print("          SOL MOVES: " + get_move_string(moves))
    else:
        print("    DFS | PASS")
        print("          SOL MOVES: " + get_move_string(moves))

    puzzle.read_puzzle(filename)
    states, moves = A_Star_H1(puzzle)
    if not states[-1].state.check_puzzle():
        print("    A*1 | FAIL")
        print("          SOL MOVES: " + get_move_string(moves))
    else:
        print("    A*1 | PASS")
        print("          SOL MOVES: " + get_move_string(moves))

    puzzle.read_puzzle(filename)
    states, moves = A_Star_H2(puzzle)
    if not states[-1].state.check_puzzle():
        print("    A*2 | FAIL")
        print("          SOL MOVES: " + get_move_string(moves))
    else:
        print("    A*2 | PASS")
        print("          SOL MOVES: " + get_move_string(moves))
    print("-" * 20)


# run_test(3, 'AI\\AssignmentA\\test_data\\ex1.txt')
# run_test(3, 'AI\\AssignmentA\\test_data\\ex2.txt')
# run_test(3, 'AI\\AssignmentA\\test_data\\ex3.txt')
# run_test(3, 'AI\\AssignmentA\\test_data\\ex4.txt')
# run_test(4, 'AI\\AssignmentA\\test_data\\ex5.txt')
# run_test(4, 'AI\\AssignmentA\\test_data\\ex6.txt')

run_test(3, "./test_data/ex1.txt")
run_test(3, "./test_data/ex2.txt")
run_test(3, "./test_data/ex3.txt")
run_test(3, "./test_data/ex4.txt")
run_test(4, "./test_data/ex5.txt")
run_test(4, "./test_data/ex6.txt")