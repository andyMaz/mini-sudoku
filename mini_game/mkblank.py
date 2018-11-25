class MkBlank:
    def __init__(self, file):
        self.file = file

    def generate_blank(self):
        f = open(self.file, 'w')
        try:
            for i in range(1, 7):
                for j in range(1, 7):
                    if j < 6:
                        temp = str(i) + str(j) + '=0, '
                    else:
                        temp = str(i) + str(j) + '=0 '
                    if j % 3 == 1:
                        print()
                        f.write('   ')
                    f.write("%s" % temp)
                    print(temp, end='')
                f.write("%s" % '\n')
                if i % 2 == 0:
                    print()
                    f.write('\n')
                print()
        finally:
            f.close()


def main():
    directory = "C:/Users/andrei/Documents/data/sudoku/mini-sudoku/"
    file_name = "mini_sudoku.txt"
    mb = MkBlank(directory + file_name)
    mb.generate_blank()


if __name__ == "__main__":
    main()
