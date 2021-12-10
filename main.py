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
        return 3
    if symbol == ']':
        return 57
    if symbol == '}':
        return 1197
    if symbol == '>':
        return 25137

    return None


def main():
    input_lines = read_file_lines()

    corrupted_symbols = []

    for line in input_lines:
        symbols = list(line)
        buffer = []
        print()

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
                    corrupted_symbols.append(sym)
                    print("Error on symbol: {}".format(sym))
                    break

    print()
    print("end of read")
    answer = 0
    for corrupted_symbol in corrupted_symbols:
        score = get_corrupted_symbol_score(corrupted_symbol)
        answer += score
        print(corrupted_symbol)

    print(answer)


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()


if __name__ == "__main__":
    main()
