def main():
    input_lines = read_file_lines()
    
    input_numbers = list(map(lambda x: int(x), input_lines[0].split(',')))

    fuel_lowest = min(input_numbers)
    fuel_highest = max(input_numbers)
    
    for num in input_numbers:
        print(num)
        
    min_sum = 9999999999
    target_fuel_cost = -1
    for x in range(fuel_lowest, fuel_highest):
        cur_fuel_cost = find_fuel_cost(input_numbers, x)
        if cur_fuel_cost < min_sum:
            min_sum = cur_fuel_cost
            target_fuel_cost = x
            
    print("target: {},  fuel: {}".format(target_fuel_cost, min_sum))


def find_fuel_cost(input_numbers, x):
    sum = 0
    for num in input_numbers:
        sum += abs(num - x)
        
    return sum


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()


if __name__ == "__main__":
    main()