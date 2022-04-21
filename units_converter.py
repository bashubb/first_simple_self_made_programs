#simple app - units converter.

class MyException(Exception):
    pass

def main_display():
    """display instuctions for user"""
    print('''
            Ten prosty program pomoże Ci przeliczyć jednostki miary, coś co zawsze tworzy problem
            Wybierz cyfrowo z mojego menu :
            1 - ciśnienie bar na psi  lub odwrotnie 
            2 - kilometry na mile lub odwrotnie
            3 - hektary na metry kwadratowe lub odwrotnie ''')


def set_how_much():
    """input how much of
    something You want to convert"""
    while True:
        try:
            give_the_number = float(input('Wprowadź wartośc jednostki do przeliczenia: '))
            break
        except ValueError:
            print('Oj! coś poszło nie tak ! Baardzo proszę podaj liczbe')
            print()

    return give_the_number

def your_choice(low, high):
    """set number of Your choice"""
    low_string = str(low)
    high_string = str(high)
    while True:
        try:
            answer = int(input(f'Bardzo prosze podaj liczbe oznaczającą twój wybór ({low_string}-{high_string}): '))
            if answer > high or answer < low:
                raise MyException(f'Użytkowniku niepoprawna  liczba! Wybierz {low_string}-{high_string} ')
            else:
                break
        except MyException as blad:
            print(blad)
            print()
        except ValueError:
            print('Oj coś poszło nie tak prosze wprowadź liczbe')
            print()

    return answer


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


def bar_psi():
    """bar_psi converter function"""
    print('''
    - Wybierz 1 jesli chcesz przeliczyć bar na psi
    - Wybierz 2 jesli chcesz przeliczyc psi na bar
        ''')
    choice = your_choice(1,2)
    how_much = set_how_much()
    if choice == 1:
        psi = how_much * 14,5
        print(f'{how_much} barów to {psi} psi ')

    else:
        bar = how_much * 0.06894757293178
        print(f'{how_much} psi to {bar} barów')


def km_mile():
    """km_mile converter function"""
    print('''
       - Wybierz 1 jesli chcesz przeliczyć km na mile
       - Wybierz 2 jesli chcesz przeliczyc mile na km
           ''')
    choice = your_choice(1, 2)
    how_much = set_how_much()
    if choice == 1:
        mile = how_much * 0.6213711922373
        print(f'{how_much} km to {mile} mile ')

    else:
        km = how_much * 1.609344
        print(f'{how_much} mil  to {km} km')


def ha_m2():
    """ha_m2 converter function"""
    print('''
       - Wybierz 1 jesli chcesz przeliczyć ha na m2
       - Wybierz 2 jesli chcesz przeliczyc m2 na ha
           ''')
    choice = your_choice(1, 2)
    how_much = set_how_much()
    if choice == 1:
        m2 = how_much * 10000
        print(f'{how_much} ha to {m2} m2 ')

    else:
        ha = how_much * 0.0001
        print(f'{how_much}  to {ha} hektarow')


# main
wanna_play_again = ''
while wanna_play_again != 'n':
    main_display()
    print()
    first_answer = your_choice(1, 3)

    if first_answer == 1:
        bar_psi()
    elif first_answer == 2:
        km_mile()
    elif first_answer == 3:
        ha_m2()


    print('Czy chcesz jeszcze coś przekonwertować t/n')
    wanna_play_again = yes_no_question()

print('Naciśnij Enter aby zakonczyć program')



