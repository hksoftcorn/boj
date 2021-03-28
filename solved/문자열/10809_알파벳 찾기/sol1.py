S = input()
arr = [-1] * 26


for idx, s in enumerate(S):
    char_idx = ord(s) - 97
    if arr[char_idx] == -1:
        arr[char_idx] = idx

print(" ".join(map(str, arr)))