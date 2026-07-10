'''
A project that requires everything I have learnt in python to make a calculator.
The first version would be the most basic way to solve it and I'd proceed to trying 
out other better and more improved ways
'''

def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b



#user_input = ''
print('''An arithmetic operation keyword guide to navigate this calculator:' 
      add: ADDITION
      sub: SUBTRACTION
      mult: MULTIPLY
      div: DIVIDE
      ''')
user_input = input('What arithmetic operation do you want to perform? ').lower()
#total = 0

if user_input == 'add':
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
        
    total = addition(a, b)
    print(total)

if user_input == 'sub':
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
        
    total = subtract(a, b)
    print(total)

if user_input == 'mult':
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
        
    total = multiply(a, b)
    print(total)

if user_input == 'div':
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
        
    total = divide(a, b)
    print(total)