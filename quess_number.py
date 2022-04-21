# User has to guess number in the range he gave himself


import random
import time


def welcome():
    print('''

                Witaj w grze jaka to liczba, twoje zadanie to zgadnąć liczbe z zakresu ktory sam podasz.   ''')


def counting(text):
    print(text)
    for i in range(5):
        print('***')
        time.sleep(1)


def ask_number(question):
    while True:
        try:
            give_the_number = int(input(question))
            break
        except ValueError:
            print('Oj! coś poszło nie tak ! Baardzo proszę podaj liczbe')

    return give_the_number


def ask_for_guess():
    guess = ask_number('Wylosowano dla Ciebie liczbę, spróbuj zgadnąc jaka to liczba. Podaj liczbe:  ')
    return guess


def yes_no_question():
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


# main
wanna_play_again = ''
while wanna_play_again != 'n':
    welcome()
    print()
    print()
    input('Jeśli jesteś gotów naciśnij Enter! ')

    give_the_range = ask_number('Wylosuje dla Ciebie cyfre od 0 do cyfry, którą podasz. Jaką cyfre wybierasz?: ')
    the_number = random.randrange(give_the_range)
    counting('losuje dla Ciebie liczbe !')
    guess = ask_for_guess()

    # check if quess == the_number
    tries = 0
    while the_number != guess:
        tries += 1
        if guess > the_number:
            print('za duża, spróbuj jeszcze raz')
            guess = ask_for_guess()

        if guess < the_number:
            print('za mała, spróbuj jeszcze raz')
            guess = ask_for_guess()

    print(f'Brawo Graczu udało Ci się zgadnąć wylosowana liczba to {the_number} udało Ci się tego dokonać w {tries}'
          f'probach', )

    print('Chcesz, zagrać jeszcze raz t/n')
    wanna_play_again = yes_no_question()

print('Użytkowniku bardzo dziekuje za wspólną grę do zobaczenia')
()
