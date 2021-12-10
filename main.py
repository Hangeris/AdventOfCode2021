import sys


def is_closing_symbol(symbol):
    return symbol == ')' or symbol == ']' or symbol == '>' or symbol == '}'


def get_opposite_symbol(symbol):
    if symbol == ')':
        return '('
    if symbol == ']':
        return '['
    if symbol == '}':
        return '{'
    if symbol == '>':
        return '<'

    if symbol == '(':
        return ')'
    if symbol == '[':
        return ']'
    if symbol == '{':
        return '}'
    if symbol == '<':
        return '>'

    return None


def get_corrupted_symbol_score(symbol):
    if symbol == ')':
        return 1
    if symbol == ']':
        return 2
    if symbol == '}':
        return 3
    if symbol == '>':
        return 4

    return None


def main():
    input_lines = read_file_lines()

    incomplete_lists = []
    

    for line in input_lines:
        symbols = list(line)
        buffer = []
        print()
        is_corrupted = False

        for sym in symbols:
            closing_symbol = is_closing_symbol(sym)
            sys.stdout.write(sym)

            if not closing_symbol:
                buffer.append(sym)
            else:
                opposite_symbol = get_opposite_symbol(sym)
                last_sym = buffer[len(buffer) - 1]
                if last_sym == opposite_symbol:
                    buffer = buffer[:-1]
                else:
                    is_corrupted = True
                    #corrupted_symbols.append(sym)
                    #print("Error on symbol: {}".format(sym))
                    break
                    
        if len(buffer) != 0 and not is_corrupted:
            buffer.reverse()
            swap_symbols(buffer)
            incomplete_lists.append(buffer)

    print()
    print("end of read")
    print()
    
    answers = []
    for incomplete_list in incomplete_lists:
        temp_answer = 0
        print(incomplete_list)

        for sym in incomplete_list:
            symbol_score = get_corrupted_symbol_score(sym)
            temp_answer = find_temp_score(temp_answer, symbol_score)
        print("temp answer: {}".format(temp_answer))
        
        answers.append(temp_answer)

    answers.sort()

    mid_index = int(len(answers)/2 - 0.5)
    print(str(answers[mid_index]))


def find_temp_score(temp_answer, symbol_score):
    return temp_answer * 5 + symbol_score

def swap_symbols(buffer):
    for i in range(0, len(buffer)):
        buffer[i] = get_opposite_symbol(buffer[i])
        


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()


if __name__ == "__main__":
    main()
