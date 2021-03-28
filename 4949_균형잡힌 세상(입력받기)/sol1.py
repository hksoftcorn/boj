
stack = []
# input_data = list(input())
input_data = list('Help( I[m being held prisoner in a fortune cookie factory)].')
for data in input_data:
    if data == '(':
        stack.append('(')
    elif data == '[':
        stack.append('[')
    elif data == ')' or data == ']':
        if stack:
            tmp = stack.pop()
            if not data == ')' and tmp == '(':
                print('NO')
                break
            elif not data == ']' and tmp == '[':
                print('NO')
                break

        else:
            print('NO')
            break
else:
    if stack:
        print('NO')
    else:
        print('YES')


