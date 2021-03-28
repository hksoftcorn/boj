number = int(input())

for num in range(1, number+1):
    if num == number:
        print(0)
    ans = num
    str_num = str(num)
    for n in str_num:
        ans += int(n)

    if ans == number:
        print(num)
        break