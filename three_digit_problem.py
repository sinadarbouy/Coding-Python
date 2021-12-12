def solution(A):
    answer = 0
    Sum = sum(A)
    desired = Sum / 2
    ln_a = len(A)
    while sum(A) > desired:
        A.sort()
        i = A[ln_a - 1]
        A[ln_a - 1] = i / 2
        answer += 1
    return answer


A = [5, 19, 8, 1]
print(solution(A))
