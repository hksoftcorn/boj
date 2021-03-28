arr = [0] + [1] * 10000

for number in range(1, 10000+1):
    d_number = 0
    d_number += number
    str_number = str(number)
    for i in range(len(str_number)):
        d_number += int(str_number[i])
    if d_number <= 10000:
        arr[d_number] = 0

for idx in range(len(arr)):
    if arr[idx]:
        print(idx)


