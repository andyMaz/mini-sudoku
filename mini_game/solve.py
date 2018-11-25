from mini_game.board import Puzzle


class Solve(object):
    def __init__(self, p, out):
        self.board = p.get_board()
        self.file = out

    def str_board(self):
        temp = ''
        for i in range(6):
            for j in range(6):
                temp += str(self.board[i][j]) + ' '
                if j % 3 == 2:
                    temp += '\t'
            temp += '\n'
            if i % 2 == 1:
                temp += '\n'
        return temp

    # for any row i, this function returns all elements
    # that are not in that row
    def row(self, i):
        s = []
        for j in range(6):
            if not (self.board[i][j] == 0):
                s.append(self.board[i][j])
        return s

    # for any column j, this function returns all elements
    # that are not in that column
    def column(self, j):
        s = []
        for i in range(6):
            if not (self.board[i][j] == 0):
                s.append(self.board[i][j])
        return s

    # for any cell (i, j) this function returns all elements
    # that are not in the same box
    def box(self, i, j):
        si = self.find_box_start_row(i)
        sj = self.find_box_start_column(j)
        s = []
        for p in range(si, si + 2):
            for q in range(sj, sj + 3):
                if not (self.board[p][q] == 0):
                    s.append(self.board[p][q])
        return s

    @staticmethod
    def find_box_start_row(n):
        return 2 * (n//2)

    @staticmethod
    def find_box_start_column(n):
        return 3 * (n//3)

    # for any cell (i, j) this function all potential possible
    # entries given the configuration of the board
    def possibilities(self, i, j):
        s = []
        if self.board[i][j] == 0:
            s.extend(self.row(i))
            s.extend(self.column(j))
            s.extend(self.box(i, j))
            return [p for p in range(1, 7) if p not in s]

    def is_unique(self, r, c):
        if not self.row_unique(r, c):
            return False
        if not self.column_unique(r, c):
            return False
        return self.box_unique(r, c)

    def row_unique(self, r, c):
        e = self.board[r][c]
        for j in range(6):
            if j != c and self.board[r][j] == e:
                return False
        return True

    def column_unique(self, r, c):
        e = self.board[r][c]
        for i in range(6):
            if i != r and self.board[i][c] == e:
                return False
        return True

    def box_unique(self, r, c):
        si = self.find_box_start_row(r)
        sj = self.find_box_start_column(c)
        e = self.board[r][c]
        for p in range(si, si + 2):
            for q in range(sj, sj + 3):
                if p != r and q != c and self.board[p][q] == e:
                    return False
        return True

    def solved(self):
        for i in range(6):
            for j in range(6):
                r = self.is_unique(i, j)
                if not r:
                    return False
        return True

    def to_file(self):
        for i in range(6):
            for j in range(6):
                self.file.write(str(self.board[i][j]) + ' ')
                if j % 3 == 2:
                    self.file.write('\t')
            self.file.write('\n')
            if i % 2 == 1:
                self.file.write('\n')

    def sudoku(self, n):
        if n < 36:
            r, c = Puzzle.index(n)
            if self.board[r][c] == 0:
                ps = self.possibilities(r, c)
                for x in ps:
                    self.board[r][c] = x  # tentative placing of value x at position n
                    self.sudoku(n + 1)
                    # checking if the game is full and a solution is found
                    if n+1 == 36 and self.solved():
                        print(self.str_board())
                        self.to_file()
                    self.board[r][c] = 0  # backtracking
            else:
                # checking if the game is full and a solution is found
                if n+1 == 36 and self.solved():
                    print(self.str_board())
                    self.to_file()
                self.sudoku(n + 1)


def main():
    pass

if __name__ == "__main__":
    main()
