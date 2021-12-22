def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        if A[i] + 1 < A[i + 1]:
            return False
    if A[0] != 1 or A[n - 1] != K:
        return False
    else:
        return True


A = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3]
K = 1

print(solution(A, K))
