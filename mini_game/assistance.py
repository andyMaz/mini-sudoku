from mini_game.solve import Solve


class Assist(object):
    def __init__(self, p, out):
        self.board = p.get_board()
        self.solve = Solve(p, out)
        self.out = out

    @staticmethod
    def line(n):
        temp = '\t'
        for _ in range(n):
            temp += '-'
        return temp

    def help(self):
        f = open(self.out, 'w')
        print()
        try:
            f.write('\n')
            for i in range(6):
                for j in range(6):
                    if self.board[i][j] == 0:
                        f.write("%9s" % self.print_lst(self.solve.possibilities(i, j)) + " ")
                        print("%9s" % self.print_lst(self.solve.possibilities(i, j)) + " ", end='')
                    else:
                        f.write("%9s" % str(self.board[i][j]) + " ")
                        print("%9s" % str(self.board[i][j]) + " ", end='')
                    if j % 3 == 2 and j != 5:
                        f.write(" |  ")
                        print(" |  ", end='')
                f.write('\n')
                print()
                if i % 2 == 1 and i != 5:
                    f.write(self.line(60) + '\n')
                    print(self.line(60))
        finally:
            f.close()

    @staticmethod
    def print_lst(ls):
        temp = ''
        for l in ls:
            temp += str(l)
        return temp
