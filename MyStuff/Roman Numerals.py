numeral_dict = {
    '1': {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '0': ''},
    '10': {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC',
           '0': ''},
    '100': {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM',
            '0': ''},
    '1000': {'1': 'M', '2': 'MM', '3': 'MMM', '4': 'MMMM'}
}


def expand(x):
    if x != 'quit':
        temp_list = []
        counter = 1
        base_number = round(int(x))
        base_number = str(base_number)

        number = base_number[::-1]
        for each_number in number:
            temp_list.append(int(each_number) * counter)
            counter *= 10
        return temp_list
    else:
        return 'quit'


def convert(num_list):
    if num_list != 'quit':
        roman_numeral = ''
        place_counter = 1
        for each_value in num_list:
            roman_numeral = numeral_dict[str(place_counter)][str(each_value)[0]] + roman_numeral
            place_counter *= 10
        if len(num_list) == 1 and num_list[0] == 0:
            roman_numeral = 'nulla'
        print('In roman numerals, your number is ' + roman_numeral + '.\n')
        return True
    else:
        return False


def check_validity(value):
    if value == 'quit':
        return True
    try:
        value = int(value)
    except ValueError:
        print('Please enter a number (the actual digits).')
        return False

    if value not in range(5000):
        print('Please enter a number between 0 and 5000 (excluding both 0 and 5000).')
        return False

    else:
        return True


converting = True
while converting:
    user_input = ''
    valid = False
    print('Enter a positive base-10 number less than 5000.')
    while not valid:
        user_input = input('> ')
        valid = check_validity(user_input)
    converting = convert(expand(user_input))
