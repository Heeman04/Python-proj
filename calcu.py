import os

while True:
    print('Select a number')
    print('1. Addition')
    print('2. Substraction')
    print('3. Multip;ication')
    print('4. Exit')
    match(input('Enter your choice:')):
        case '1':
           a = int(input('Entr first number:'))
           b = int(input('Entr second number:'))
           print(f'{a} + {b} is {a+b}')
        case '2':
           a = int(input('Entr first number:'))
           b = int(input('Entr second number:'))
           print(f'{a} - {b} is {a-b}')
        case '3':
           a = int(input('Entr first number:'))
           b = int(input('Entr second number:'))
           print(f'{a} * {b} is {a*b}')
        case'4':
           print('Exiting...')
           break
        case _:
            print('Invalid Choice')
            input('Press enter to continue...')
            os.system('cls')