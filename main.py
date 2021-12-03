def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()

def main():
    input_lines = read_file_lines()

    depth = 0
    position = 0
    aim = 0

    for line in input_lines:
        dir = line.split(" ")[0]
        amount = int(line.split(" ")[1])

        if dir == "up":
            aim -= amount

        elif dir == "down":
            aim += amount

        elif dir == "forward":
            position += amount
            depth += aim * amount



    print(str(position * depth))



if __name__ == "__main__":
    main()