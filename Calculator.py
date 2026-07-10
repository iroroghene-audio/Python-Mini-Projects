'''
A project that requires everything I have learnt in python to make a calculator.
The second version of the app and it minimizes repetition, thus making the codbase cleaner
And a loop is introduced so it doesn't just quit after one calculation is completed
'''

def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print('''An arithmetic operation keyword guide to navigate this calculator:' 
      add: ADDITION
      sub: SUBTRACTION
      mult: MULTIPLY
      div: DIVIDE
      ''')

#MAIN CONTROL
result = 0
while True:
        user_input = input('What arithmetic operation do you want to perform? ').lower()
        
        if user_input not in ['add','sub','mult','div','quit']:
            print('Invalid Operation! Enter a valid keyword!')
        elif user_input == 'quit':
            break
        else:
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))

            if user_input == 'add':
                result = addition(a, b)


            elif user_input == 'sub':
                result = subtract(a, b)


            elif user_input == 'mult':
                result = multiply(a, b)


            elif user_input == 'div':
                if b == 0:
                    print('Zero Error')
                    continue
                else:
                    result = divide(a, b)
   
            print(result)
            
            