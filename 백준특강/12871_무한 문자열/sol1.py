a = input()
b = input()

a_length = len(a)
b_length = len(b)

if (a * b_length) == (b * a_length):
    print(1)
else:
    print(0)