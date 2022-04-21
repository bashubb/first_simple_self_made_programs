# display name gave by user on the screen


name = input('Jak masz na imię?: ')

while True:
    if name.isalpha():
        break
    else:
        print('Imię musi być złożone z liter')
        print()
        name = input('Jak masz na imię?: ')

welcome = print(f'Witaj {name.title()}')
