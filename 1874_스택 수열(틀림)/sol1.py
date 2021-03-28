import sys
sys.stdin = open('input.txt', 'r')


def solution(number):
    global stack, result, last_num

    if number > last_num:
        for num in range(last_num + 1, number + 1):
            stack.append(num)
            result.append('+')
        last_num = num
        result += ['-']
        stack.pop()
    else:
        while 1:
            result += ['-']
            if len(stack) == 0 or number > stack[-1]:
                result = []
                return result
            tmp = stack.pop()
            if number == tmp:
                break

    return result


T = int(input())
stack = []
result = []
last_num = 0

for tc in range(1, T + 1):
    number = int(input())
    solution(number)

if result:
    for r in result:
        print(r)
else:
    print('NO')
