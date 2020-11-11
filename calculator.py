import sys

if len(sys.argv) != 4:
    print('You must provide 3 parameters')
else:
    x = sys.argv[2]
    y = sys.argv[3]

    if sys.argv[1] == '+':
        z = int(x) + int(y)
    elif sys.argv[1] == '-':
        z = int(x) - int(y)
    elif sys.argv[1] == 'x':
        z = int(x) * int(y) 
    elif sys.argv[1] == '/':
        z = int(x) / int(y)
    elif sys.argv[1] == '^':
        z = int(x) % int(y)
    else:
        print('You have provided an invalid operator!')
        z = None

    if z != None: 
        print(z)