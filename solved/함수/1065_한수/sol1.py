
def solution(N):
    if N < 100:
        return N
    elif N == 1000:
        return 144
    else:
        cnt = 99
        for number in range(100, N+1):
            new_number = str(number)
            a, b, c = new_number[0], new_number[1], new_number[2]
            if (int(a) - int(b)) == (int(b) - int(c)):
                cnt += 1
        return cnt


print(solution(int(input())))