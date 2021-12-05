class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print("Entry  {:3}x {:3}y".format(self.x, self.y))
     
        
class Entry:
    def __init__(self, raw_line_input):
        split_raw_line = raw_line_input.split(" -> ")
        self.x1 = int(split_raw_line[0].split(',')[0])
        self.y1 = int(split_raw_line[0].split(',')[1])
        self.x2 = int(split_raw_line[1].split(',')[0])
        self.y2 = int(split_raw_line[1].split(',')[1])
        
        self.points = []
        if self.x1 == self.x2:
            print("{:2}x are equal. range from {:2} to {:2}".format(self.x1, self.y1, self.y2))
            increment_amount = 1 if self.y1 < self.y2 else -1
            for y in range(self.y1, self.y2 + increment_amount, increment_amount):
                self.points.append(Point(self.x1, y))

        if self.y1 == self.y2:
            print("{:2}y are equal. range from {:2} to {:2}".format(self.y1, self.x1, self.x2))
            increment_amount = 1 if self.x1 < self.x2 else -1
            for x in range(self.x1, self.x2 + increment_amount, increment_amount):
                self.points.append(Point(x, self.y1))
                
    def is_diagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2

    def show(self):
        print("{:2},{:2} -> {:2},{:2}  has these points v".format(self.x1, self.y1, self.x2, self.y2))
        for point in self.points:
            point.show()
        
        
def main():
    input_lines = read_file_lines()
    
    entries = []
    for line in input_lines:
        entry = Entry(line)
        entries.append(entry)
        
    grid = {}
    for entry in entries:
        if entry.is_diagonal():
            continue
            
        for point in entry.points:
            point_key = (point.x, point.y)
            if not grid.__contains__(point_key):
                grid[point_key] = 0
            grid[point_key] += 1
            
    answer = 0
    for point in grid:
        if grid[point] >= 2:
            answer += 1
         
    print(answer)


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()


if __name__ == "__main__":
    main()