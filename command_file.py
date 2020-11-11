import sys
import math
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

goto_line = 1
last_goto_line = 0
lines_visited = []
visited_before = False
while visited_before == False:

    split_line = lines[goto_line-1].split()

    if split_line[1] == 'calc':
        result = calculate(split_line[2], int(split_line[3]), int(split_line[4]))
        goto_line = math.floor(result)
        lines_visited.append(goto_line)

    else:
        goto_line = int(split_line[1])
        lines_visited.append(goto_line)
    
    contains_duplicates = any(lines_visited.count(element) > 1 for element in lines_visited)
    if contains_duplicates == True:
        visited_before = True
         
    

    print(goto_line)
    
    

print(f'First repeated line visit is: {goto_line}')





    



