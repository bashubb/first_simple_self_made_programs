# Find your special name from Harry Potter
import random
import time

NAMES = ['Harry Potter', 'Hermiona Granger', 'Ron Weasley', 'McGonagall',
         'Hargrid', 'Dumbledor', 'Syrius Black']

def give_me_name():
    """Function returns name gaven by user"""

    name = input("\t\tPodaj swoje imię: ")
    while True:
        if isinstance(name, str):
            break
        else:
            print('Imię musi skłdać sie z liter! spróbuj jeszcze raz!')
            name = input("\t\tPodaj swoje imię: ")
    big_name = name.title()
    return big_name


def welcome_display(user_name):
    """Displays welcome"""

    print(f'''
                Witaj {user_name}  w grze - Znajdz swoje imię z Harrego Pottera ''')


def counting(text):
    """Counting animation"""

    print(text)
    for i in range(5):
        print('***')
        time.sleep(1)

def yes_no_question():
    """Returns answer y/n (t/n)"""

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




#main
yes_or_no = ''
while yes_or_no != 'n':
    user_name = give_me_name()
    welcome_display(user_name)
    print('================================================'
          '====================================================')
    name_from_HP = random.choice(NAMES)
    counting('\t\tUważaj losuje teraz twoję nowe imię z Harrego Pottera ')
    print('================================================='
          '===================================================')
    print(f'''
                    {user_name} twoje nowe imię z sagi Harry Potter to {name_from_HP} !!! mam nadzieje,że 
                        Ci sie podoba ''')

    print('================================================='
          '===================================================')
    print('\t\tCzy chcesz polosować jeszcze raz? (tak/nie)')
    yes_or_no = yes_no_question()

print('Dziekuje za wspolną grę, do zobacznia')
input('Naciśnij Enter, aby zakończyć')