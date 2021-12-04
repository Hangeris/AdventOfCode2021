import io

class Entry:
    def __init__(self, number):
        self.number = number
        self.is_marked = False

    def mark(self):
        self.is_marked = True


class Board:
    def __init__(self, width):
        self.width = width
        self.board = [[0 for i in range(width)] for j in range(width) ]
        self.row_id = 0
        
    def add_row(self, row_string):
        row_string_split = row_string.split()
        for i in range(0, len(row_string_split)):
            self.board[self.row_id][i] = Entry(int(row_string_split[i]))
        self.row_id += 1

    def mark_number(self, number):
        for i in range(0, self.width):
            for j in range(0, self.width):
                if self.board[i][j].number != number:
                    continue

                self.board[i][j].mark()

    def is_complete(self):
        for i in range(0, self.width):
            marked_count = 0
            for j in range(0, self.width):
                if self.board[i][j].is_marked is True:
                    marked_count += 1
            if marked_count == 5:
                return True

        for i in range(0, self.width):
            marked_count = 0
            for j in range(0, self.width):
                if self.board[j][i].is_marked is True:
                    marked_count += 1
            if marked_count == 5:
                return True

        return False

    def find_unmarked_sum(self):
        sum = 0
        for i in range(0, self.width):
            for j in range(0, self.width):
                if self.board[i][j].is_marked is False:
                    sum += self.board[i][j].number
        return sum

    def show(self):
        print("is complete: {}".format(str(self.is_complete())))
        for i in range(0, self.width):
            print("{:2} {:2} {:2} {:2} {:2}".format(self.board[i][0].number, self.board[i][1].number, self.board[i][2].number, self.board[i][3].number, self.board[i][4].number))
        print()
                

def main():
    input_lines = read_file_lines()

    drawn_numbers = list(map(int, (input_lines[0].split(",")))) 
    print(drawn_numbers)

    boards = []
    for line in input_lines[1:]:
        if len(line) == 0:
            board = Board(5)
            boards.append(board)
            continue
        
        board.add_row(line)
  
    for drawn_number in drawn_numbers:
        for board in boards:
            board.mark_number(drawn_number)
            if board.is_complete():
                board.show()
                sum = board.find_unmarked_sum()
                print("answer: {}".format(sum * drawn_number))
                return


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()

if __name__ == "__main__":
    main()