class Data:
    def __init__(self, decimal_string, decimal):
        self.decimal_string = decimal_string
        self.decimal = decimal

def main():
    input_lines = read_file_lines()

    datas = []
    for line in input_lines:
        data = Data(line, int(line, 2))
        datas.append(data)


    gamma_decimal = 0
    bit_length = len(data.decimal_string)
    for i in range(0, bit_length):
        shifted_decimal = 1 << i

        has = 0
        have_not = 0

        for data in datas:
            if (data.decimal & shifted_decimal == shifted_decimal):
                has += 1
            else:
                have_not += 1

        if (has > have_not):
            gamma_decimal += shifted_decimal


    bit_length_decimal = (1 << bit_length) - 1
    print("bitLength count: {}".format(bit_length))
    print("bitLength in decimal: {}".format(bit_length_decimal))
    print("gamma decimal: {}".format(gamma_decimal))
    print("epsilon rate: {}".format(int(bit_length_decimal)-gamma_decimal))
    print(gamma_decimal * ((bit_length_decimal)-gamma_decimal))

    


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()

if __name__ == "__main__":
    main()