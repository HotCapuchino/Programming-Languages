math_statement = input('Please enter math statement: ')
num1 = ''
num2 = ''
action = ''
math_signs = ['+', '-', '/', '*']
i = 0
while math_statement[i] not in math_signs or ord(math_statement[i]) == 160:
    num1 += math_statement[i]
    i += 1
while ord(math_statement[i]) == 160:
    i += 1
action = math_statement[i]
i += 1
while i < len(math_statement):
    if math_statement[i] not in math_signs and math_statement[i]:
        num2 = math_statement[i]
    i += 1
print(num1, action, num2)
try:
    if action == '+':
        print(f'{int(num1) + int(num2)}')
    elif action == '-':
        print(f'{int(num1) - int(num2)}')
    elif action == '/':
        print(f'{int(num1) / int(num2)}')
    elif action  == '*':
        print(f'{int(num1) / int(num2)}')
except:
    print('something went wrong!')

