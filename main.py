def main():
    input_lines = read_file_lines()
    for line in input_lines:
        print(line)


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()


if __name__ == "__main__":
    main()