T = int(input())
cnt = T
for tc in range(1, T+1):
    S = input()
    my_list = []
    for s in S:
        if s not in my_list:
            my_list.append(s)
        elif s == my_list[-1]:
            pass
        else:
            cnt -= 1
            break
print(cnt)


