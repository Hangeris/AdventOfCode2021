def main():
    input_lines = read_file_lines()
    
    prev_sum = -1
    prev_list = [-1, -1, -1]
    increments = 0

    for line in input_lines:
        num = int(line)

        del prev_list[-1]
        prev_list.insert(0, num)

        cur_sum = find_current_sum(prev_list)
        if prev_sum != -1 and cur_sum > prev_sum:
            increments += 1

        prev_sum = cur_sum

    print(increments)


def find_current_sum(numbers):
    if numbers.__contains__(-1):
        return -1

    sum = 0
    for number in numbers:
        sum += number

    return sum


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()


if __name__ == "__main__":
    main()
