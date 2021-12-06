import sys

class LanternFishStack:
    def __init__(self, starting_day, amount):
        self.health = starting_day
        self.amount = amount

    def decrease(self):
        self.health -= 1
    

def main():
    input_lines = read_file_lines()
    
    fishes = []
    input_in_days = input_lines[0].split(',')
    for input_in_day in input_in_days:
        fishes.append(LanternFishStack(int(input_in_day), 1))

    show(fishes)
    amount = 0
    
    for i in range(0, 256):
        for fish in fishes:
            if fish.health <= 0:
                amount += fish.amount
                fish.health = 6
            else:
                fish.health -= 1

        if amount != 0:
            fishes.append(LanternFishStack(8, amount))
            amount = 0
            
        #show(fishes)
    
    answer = 0
    for fish in fishes:
        answer += fish.amount
    print(answer)


def show(fishes):
    for fish in fishes:
        sys.stdout.write("{}({}),".format(fish.health, fish.amount))
    print()
        

def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()


if __name__ == "__main__":
    main()