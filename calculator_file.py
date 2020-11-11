import sys
filename = sys.argv[1]
total = 0

def calculate(operator, x, y):
    if operator == '+':
        z = x + y
    elif operator == '-':
        z = x - y
    elif operator == 'x':
        z = x * y 
    elif operator == '/':
        z = x / y
    else:
        z = 'Error!'

    return z

with open(filename, 'r') as f:
    lines = f.readlines()

with open("step_2_out.txt", 'w') as f:
    for line in lines:
        calc = line.split()

        result = calculate(calc[1], int(calc[2]), int(calc[3]))
        total = total + result
        
        print(f'{calc[2]} {calc[1]} {calc[3]} = {str(result)}')
        
        f.write(f'{calc[2]} {calc[1]} {calc[3]} = {str(result)}\n')
    
print(f'Grand Total: {total}')

