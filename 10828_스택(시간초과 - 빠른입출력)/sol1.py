import sys
sys.stdin = open('input.txt', 'r')


def push(x):
    return stack.append(x)


def pop():
    if not stack:
        print(-1)
    else:
        print(stack.pop())


def size():
    print(len(stack))


def empty():
    if stack:
        print(0)
    else:
        print(1)


def top():
    if not stack:
        print(-1)
    else:
        print(stack[-1])


global stack
stack = []


N = int(input())
for _ in range(N):
    input_data = list(input().split())
    func = input_data[0]
    if func == 'push':
        push(input_data[1])
    elif func == 'pop':
        pop()
    elif func == 'size':
        size()
    elif func == 'empty':
        empty()
    else:
        top()





