import sys

class LanternFish:
    def __init__(self, starting_day):
        self.health = starting_day

    def decrease(self):
        self.health -= 1

def main():
    input_lines = read_file_lines()
    
    fishes = []
    input_in_days = input_lines[0].split(',')
    for input_in_day in input_in_days:
        fishes.append(LanternFish(int(input_in_day)))

    show(fishes)
    upcoming_fishes = []
    
    for i in range(0, 80):
        for fish in fishes:
            if fish.health <= 0:
                upcoming_fishes.append(LanternFish(8))
                fish.health = 6
            else:
                fish.health -= 1

        fishes.extend(upcoming_fishes)
        upcoming_fishes = []
        #show(fishes)
    
    print(len(fishes))

def show(fishes):
    for fish in fishes:
        sys.stdout.write("{},".format(fish.health))
    print()
        

def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()

if __name__ == "__main__":
    main()