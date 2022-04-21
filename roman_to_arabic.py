# arabic to roman/ roman to arabic converter

class MyException(Exception):
    """Class of my Exception"""
    pass


ROMAN_ARABIC = {
    'ones': {
        '1': 'I',
        '4': 'IV',
        '5': 'V',
        '9': 'IX',
    },
    'tens': {
        '1': 'X',
        '4': 'XL',
        '5': 'L',
        '9': 'XC',
    },
    'hundreds': {
        '1': 'C',
        '4': 'CD',
        '5': 'D',
        '9': 'CM',
    },
    'thousands': {
        '1': 'M'
    }
}


def welcome_display():
    """Function displays welcome"""
    print('''
                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    Witaj w programie konwerter liczb arabskich - rzymskich
                ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        ''')


def ask_number(question, low, high):
    while True:
        try:
            give_the_number = int(input(question))
            if give_the_number > high or give_the_number < low:
                raise MyException
            break
        except ValueError:
            print('!!!!!!!!!!!!!!')
            print('Oj! coś poszło nie tak ! Baardzo proszę podaj liczbe')
        except MyException:
            print('!!!!!!!!!!!!!!')
            print('Musisz wprowadzic liczbe pomiedzy 1 i 2 ')

    return give_the_number


def main_menu():
    """Returns number of transform option choosen by user"""

    print('''
                    1 - z Arabskich na Rzymskie 
                    2 - z Rzymskich na Arabskie
                    ''')
    print()
    which_way = ask_number('wybierz 1 lub 2 ', 1, 2)
    return which_way


def enter_arabic():
    """Function which returns arabic number given by user"""

    print('-------------------')
    print('Wybrałeś konwersje z cyfr Arabskich na Rzymskie')
    while True:
        give_arabic = (input('Wprowadź liczbe Arabską: '))
        if give_arabic.isnumeric():
            break
        else:
            print('!!!!!!!!!!!!!!')
            print("wprowadź cyfre arabską składającą sie ze znków 0 - 9")

    return give_arabic


def arabic_in_pieces(value, name_part_of_number):
    """Function which prepares roman number to be transformed to arabic"""

    if int(value) <= 3:
        return ROMAN_ARABIC[name_part_of_number]['1'] * int(value)
    if int(value) == 4:
        return ROMAN_ARABIC[name_part_of_number][value]
    if int(value) == 5:
        return ROMAN_ARABIC[name_part_of_number][value]
    if int(value) > 5 and int(value) < 9:
        return ROMAN_ARABIC[name_part_of_number]['5'] + ROMAN_ARABIC[name_part_of_number]['1'] * (int(value) - 5)
    if int(value) == 9:
        return ROMAN_ARABIC[name_part_of_number]['9']


def transform_arabic_to_roman():
    """Function which transforms arabic number into roman number"""

    arabic = enter_arabic()
    arabic_list = list(arabic)
    arabic_list.reverse()
    ones = ''
    tens = ''
    hundreds = ''
    thousands = ''
    for index, value in enumerate(arabic_list):
        if index == 0:
            ones = arabic_in_pieces(value, 'ones')
        elif index == 1:
            tens = arabic_in_pieces(value, 'tens')
        elif index == 2:
            hundreds = arabic_in_pieces(value, 'hundreds')
        elif index == 3:
            thousands = arabic_in_pieces(value, 'thousands')

    final_roman = thousands + hundreds + tens + ones

    return final_roman, arabic


def enter_roman():
    """Funcion which returns roman number given by user"""

    print('-------------------')
    print('Wybrałeś konwersje z cyfr Rzymskich na Arabskie')
    while True:
        give_roman = (input('Wprowadź liczbe Rzymską: '))
        if give_roman.isupper():
            break
        else:
            print('!!!!!!!!!!!!!!')
            print('Wprowaadź liczbe Rzymską składającą się z dużych liter')

    return give_roman


def roman_in_pieces(roman_list, first, second):
    """Function which prepares roman number to be transformed to arabic"""

    for index, item in enumerate(roman_list):
        if item == first and index == len(roman_list) - 1:
            break
        elif item == first and roman_list[index + 1] == second:
            first_in_tuple = roman_list.pop(index)
            second_in_tuple = roman_list.pop(index)
            roman_list.append(first_in_tuple + second_in_tuple)


def transform_roman_to_arabic():
    """Function which converts roman number into arabic number """

    roman = enter_roman()
    roman_list = list(roman)
    roman_in_pieces(roman_list, 'I', 'V')
    roman_in_pieces(roman_list, 'I', 'X')
    roman_in_pieces(roman_list, 'X', 'C')
    roman_in_pieces(roman_list, 'X', 'L')
    roman_in_pieces(roman_list, 'C', 'D')
    roman_in_pieces(roman_list, 'C', 'M')

    arabic = []

    for item in roman_list:
        for key, value in ROMAN_ARABIC['ones'].items():
            if item == value:
                arabic.append(int(key))
        for key, value in ROMAN_ARABIC['tens'].items():
            if item == value:
                arabic.append(int(key) * 10)
        for key, value in ROMAN_ARABIC['hundreds'].items():
            if item == value:
                arabic.append(int(key) * 100)
        for key, value in ROMAN_ARABIC['thousands'].items():
            if item == value:
                arabic.append(int(key) * 1000)

    final_arabic = sum(arabic)
    return final_arabic, roman


def yes_no_question():
    """returns answer y/n (t/n)"""

    answer = input().lower()
    while True:
        try:
            if answer.isalpha() and (answer.startswith('t') or answer.startswith('n')):
                break
            raise Exception
        except Exception:
            print('!!!!!!!!!!!!!!')
            print('To jest pytanie tak/nie - wprowadz tak lub nie ')
            answer = input().lower()
    return answer[0]


# main
wanna_play_again = ''
while wanna_play_again != 'n':

    welcome_display()
    choice = main_menu()
    if choice == 1:
        transformed_to_roman, arabic = transform_arabic_to_roman()
        print(f'''Liczba arabska {arabic} została przekonwertowana na Liczbe rzymską 
                            ------- {transformed_to_roman}  -------- ''')
        print('============================================================')
    else:
        transformed_to_arabic, roman = transform_roman_to_arabic()
        print(f'''Liczba rzymska {roman} została przekonwertowana na Liczbe araabską 
                            ------- {transformed_to_arabic} ---------''')
        print('============================================================')

    print('Czy chcesz jeszcze coś przekonwertować t/n')
    wanna_play_again = yes_no_question()
