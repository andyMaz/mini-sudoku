
# from game.gui import SudokuGUI
# from tkinter import *
from mini_game.board import Puzzle
from mini_game.solve import Solve
from mini_game.assistance import Assist


def main():
    directory = "C:/Users/andrei/Documents/data/sudoku/mini-sudoku/"
    filename = "mini_sudoku.txt"
    p = Puzzle(directory + filename)

    p.read_puzzle()
    print(p)
    print('----------')

    out = open(directory + "solution.txt", 'w')
    try:
        sl = Solve(p, out)
        sl.sudoku(0)
        a = Assist(p, directory + "mini_assist.txt")
        a.help()
    finally:
        out.close()


if __name__ == "__main__":
    main()
