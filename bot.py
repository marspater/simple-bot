def greet(bot_name, birth_year):
    print("Hello! My name is " + bot_name + ". I'm a simple bot.")
    print('I was created in ' + birth_year + ' by Olek.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print()
    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')
    print()

    num = int(input())
    curr = 0
    print()
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    print()
    print("Let's test your programming knowledge.")
    print()
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    answer = int(input())
    while answer != 2:
        print('Please, try again.')
        answer = int(input())
    if answer == 2:
        end()

def end():
    print()
    print('Congratulations, have a nice day!')


greet('Mars', '2020')  # change it as you need
remind_name()
guess_age()
count()
test()
# ...
