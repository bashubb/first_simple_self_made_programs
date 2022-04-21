# password generator


import random
import string


class MyException(Exception):
    pass


marks = {
    'małe litery': string.ascii_lowercase,
    'duże litery': string.ascii_uppercase,
    'liczby': string.octdigits,
    'znaki specjalne': string.punctuation
}


def welcome_display():
    """Function wi"""
    print('''
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                Witaj w programie, który wygeneruje dla Ciebie hasło!! 
                                wszystko co musisz zrobić to odpowiedz na kilka pytań
            ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ''')
    input('\n\t\t\t\t\tJeśli jesteś gotów naciśnij ENTER ! ')
    print()


def yes_no_question():
    """returns answer y/n (t/n)"""
    answer = input().lower()
    while True:
        try:
            if answer.isalpha() and (answer.startswith('t') or answer.startswith('n')):
                break
            raise Exception
        except Exception:
            print('To jest pytanie tak/nie - wprowadz tak lub nie ')
            answer = input().lower()
    return answer[0]


def question(mark, mark_name):
    print('=====================')
    print(f'Czy chcesz, aby w towim haśle znajdowały sie {mark_name} (tak/nie): ')
    answer = yes_no_question()
    if answer == 't':
        return mark
    if answer == 'n':
        return ''


def how_much_marks():
    while True:
        try:
            give_the_number = int(input("Podaj ile znaków ma mieć hasło (1- 15): "))
            if give_the_number > 15 or give_the_number < 1:
                raise MyException('Hasło musi miec 1-15 znaków, Spróbuj jeszcze raz')
            break
        except ValueError:
            print('Oj! coś poszło nie tak ! Baardzo proszę podaj liczbe')
        except MyException as moj_blad:
            print(moj_blad)

    return give_the_number


# main

welcome_display()

while True:
    lower = question(marks['małe litery'], 'małe litery')
    upper = question(marks['duże litery'], 'duże litery')
    numbers = question(marks['liczby'], 'liczby')
    special_marks = question(marks['znaki specjalne'], 'znaki specjalne')
    make_base_of_marks = lower + upper + numbers + special_marks
    if make_base_of_marks != '':
        break
    else:
        print('W twoim haśle musi znajdować sie jakaś kategoria znaków, musisz dokonać wyboru chociaż jednej kategorii'
              'Spróbuj jeszcze raz')


how_long_password = how_much_marks()
make_base_of_marks = list(make_base_of_marks)
random.shuffle(make_base_of_marks)
password = ''.join([letter for letter in make_base_of_marks[:how_long_password]])
print()
print(f'\t\t\tTwoje hasło to ------ {password} --------')
