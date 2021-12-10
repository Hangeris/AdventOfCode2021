import sys;


def main():
    input_lines = read_file_lines()

    numbers = []

    for line in input_lines:
        line_numbers = [int(x) for x in line]
        numbers.append(line_numbers)
        print(line)

    lowest_numbers = []
    for x in range(0, len(numbers)):
        line_numbers = numbers[x]
        for y in range(0, len(line_numbers)):
            #sys.stdout.write(str(line_numbers[y]) + " ")
            nearby_numbers = find_nearby_numbers(numbers, line_numbers, x, y)
            lowest_number = find_lowest_number(numbers[x][y], nearby_numbers)
            if lowest_number == -1:
                continue

            lowest_numbers.append(numbers[x][y])
                
    answer = 0
    for num in lowest_numbers:
        answer += 1 + num
        #print(num)
    print(answer)

    # for line_numbers in numbers:
    #     for number in line_numbers:
    #         sys.stdout.write(str(number) + " ")
    #     print()
    #     print()
    #     

def find_lowest_number(number, nearby_numbers):
    lowest = 999999999999
    for num in nearby_numbers:
        if num < lowest:
            lowest = num
            
    if number < lowest:
        return number
    
    return -1


def find_nearby_numbers(numbers, line_numbers, x, y):
    nearby_numbers = []

    max_length_x = len(numbers)
    max_length_y = len(line_numbers)

    if is_coordinate_in_bounds(x - 1, y, max_length_x, max_length_y):
        nearby_numbers.append(numbers[x - 1][y])

    if is_coordinate_in_bounds(x + 1, y, max_length_x, max_length_y):
        nearby_numbers.append(numbers[x + 1][y])

    if is_coordinate_in_bounds(x, y - 1, max_length_x, max_length_y):
        nearby_numbers.append(numbers[x][y - 1])

    if is_coordinate_in_bounds(x, y + 1, max_length_x, max_length_y):
        nearby_numbers.append(numbers[x][y + 1])

    return nearby_numbers


def is_coordinate_in_bounds(x, y, max_length_x, max_length_y):
    return 0 <= x < max_length_x and 0 <= y < max_length_y


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()


if __name__ == "__main__":
    main()
