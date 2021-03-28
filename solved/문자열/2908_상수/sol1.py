a, b = map(str, input().split())
new_a = int(a[::-1])
new_b = int(b[::-1])
if new_a > new_b:
    print(new_a)
else:
    print(new_b)