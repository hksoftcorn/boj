T  = int(input())

for _ in range(T):
    stack = []
    input_data = list(input())
    for data in input_data:
        if data == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
