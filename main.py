class Data:
    def __init__(self, decimal_string, decimal):
        self.decimal_string = decimal_string
        self.decimal = decimal

def main():
    input_lines = read_file_lines()

    datas = []
    datas2 = []
    for line in input_lines:
        data = Data(line, int(line, 2))
        datas.append(data)
        datas2.append(data)

    #oxygen generator rating
    bit_length = len(data.decimal_string)
    for i in range(0, bit_length): 
        shifted_decimal = 1 << ((bit_length-1) - i)

        data_has = []
        data_has_not = []

        for data in datas:
            if (data.decimal & shifted_decimal == shifted_decimal):
                data_has.append(data)
            else:
                data_has_not.append(data)

        if (len(data_has) >= len(data_has_not)):
            datas = [ele for ele in datas if ele not in data_has_not]
        else:
            datas = [ele for ele in datas if ele not in data_has]

        if len(datas) == 1:
            break

    #CO2 scrubber rating
    for i in range(0, bit_length): 
        shifted_decimal = 1 << ((bit_length-1) - i)

        data_has = []
        data_has_not = []

        for data in datas2:
            if (data.decimal & shifted_decimal == shifted_decimal):
                data_has.append(data)
            else:
                data_has_not.append(data)

        if (len(data_has_not) <= len(data_has)):
            datas2 = [ele for ele in datas2 if ele not in data_has]
        else:
            datas2 = [ele for ele in datas2 if ele not in data_has_not]

        if len(datas2) == 1:
            break

    bit_length_decimal = (1 << bit_length)
    print("bitLength count: {}".format(bit_length))
    print("bitLength in decimal: {}".format(bit_length_decimal))
    oxygen_generator_rating = datas[0].decimal
    co2_scrubber_rating = datas2[0].decimal
    print(oxygen_generator_rating)
    print(co2_scrubber_rating)
    print(oxygen_generator_rating * co2_scrubber_rating)

    


def read_file_lines():
    return open('input.txt', 'r', encoding='utf-8-sig').read().splitlines()

if __name__ == "__main__":
    main()