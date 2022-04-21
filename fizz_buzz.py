"""
FizzBuzz - count from 0 to 100
if number is divisible by 3 display 'Fizz'
if number is divisible by 5 display 'Buzz'
if number is divisible by 3 and 5 display 'FizzBuzz'
"""

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number, 'FizzBuzz')
    elif number % 3 == 0:
        print(number, 'Fizz')
    elif number % 5 == 0:
        print(number, 'Buzz')
