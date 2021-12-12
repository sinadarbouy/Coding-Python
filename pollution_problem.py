def maximum(a, b):

    if a >= b:
        return a
    else:
        return b


def solution(N, K):
    if K == 0:
        return N
    ln = len(str(N))
    max = maximum(int(N), K)
    for i in range(ln - 1):
        for m in range(i + 1, ln):
            if int(str(N)[i]) < int(str(N)[m]):
                str(N)[i], str(N)[m] = str(N)[m], str(N)[i]
                print("in ")
                if int(N) > max:
                    max = N
                max = maximum(int(N), K - 1)
                str(N)[i], str(N)[m] = str(N)[m], str(N)[i]

    return max


N = 592
K = 4
print(solution(N, K))
