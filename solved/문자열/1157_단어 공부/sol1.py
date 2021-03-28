S = input().upper()
arr = [0] * 26
for s in S:
    arr[ord(s) - 65] += 1

ans = [idx for idx, x in enumerate(arr) if x == max(arr)]

if len(ans) > 1:
    print('?')
else:
    print(chr(ans[0]+ 65))