import csv


class Puzzle(object):
    def __init__(self, in_file):
        self.in_file = in_file
        self.board = [[0 for _ in range(6)] for _ in range(6)]

    def get_board(self):
        return self.board

    def __str__(self):
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

    def read_puzzle(self):
        f = open(self.in_file, 'rt')
        try:
            reader = csv.reader(f)
            for row in reader:
                for e in row:
                    cs = e.split('=')
                    c = int(cs[0].strip())
                    if cs[1].strip() == '':
                        v = int('0')
                    else:
                        v = int(cs[1].strip())
                    x = c // 10
                    y = c - (x * 10)
                    self.board[x - 1][y - 1] = v
                # print()
        finally:
            f.close()

    @staticmethod
    def index(n):
        r = n // 6
        c = n % 6
        return r, c
