print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
def math():
    C_to_F = input('Convert C to F? True/False')
    if C_to_F == "False":
        num_1 = float(input('Input a number'))
        operator = input('Input an operator (+,-,*,/)')
        num_2 = float(input('Input a number'))
    else: 
        num_1 = float(input('Input a number to convert to F'))
    if C_to_F=="True":
        answer = num_1*9/5 + 32
    elif operator =='+':
        answer = num_1 + num_2
    elif operator =='-':
        answer = num_1 - num_2
    elif operator =='*':
        answer = num_1 * num_2
    elif operator =='/':
        answer = num_1 / num_2
    else:
        answer = 0
    if C_to_F=="True":
        what_to_return = print(f'{num_1} degrees C is equal to {answer} degrees F.')
    else:
        what_to_return = print(f'{num_1} {operator} {num_2} is equal to {answer}.')
    return what_to_return
    
math()