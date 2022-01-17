def missing_number(number_list) -> int:

    expected = len(number_list)+1
    missing_number = 0
    for bit_index in range(32):
        zeros = 0
        ones = 0
        for i in number_list:
            zeros = zeros + 1 if  ((i >> bit_index) & 1) == 0 else zeros
            ones = ones + 1 if  ((i >> bit_index) & 1) == 1 else ones
        print(f"{bit_index}: {expected} | {zeros} - {ones} -> {missing_number}")
        if (zeros - ones > 0):
            # bit of missing number is 1
            missing_number |= (1 << bit_index)
            expected -= zeros
            discard_numbers_with_bit(number_list, bit_index, 0)

        if (zeros - ones == 0):
            # bit of missing number is 0
            expected -= ones
            discard_numbers_with_bit(number_list, bit_index, 1)
            
        if expected == 1: break

    return missing_number


def discard_numbers_with_bit(array, index, value):
    for i in array:
        if ( (i >> index) & 1) == value:
            array.remove(i)
