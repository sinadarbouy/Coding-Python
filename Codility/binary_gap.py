"""
A binary gap within a positive integer N is any maximal sequence of
 consecutive zeros that is surrounded by ones at both ends in the binary
 representation of N.
"""


def solution2(N):
    count = 0
    maxCount = 0
    while N:
        if N & 1 == 0:
            count += 1
        else:
            maxCount = max(maxCount, count)
            count = 0
        N >>= 1

    return maxCount


def solution(N):
    number = bin(N)[2:]
    maxCount = 0
    count = 0
    for n in number:
        if n == "0":
            count += 1
        else:
            if maxCount < count:
                maxCount = count
                count = 0
            else:
                count = 0
    return maxCount


"""
529 ->4
"""
print(solution2(529))
