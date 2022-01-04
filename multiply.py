def multiply(a, b, sum=0):
    if b == 0:
        return sum
    else:
        sum += a
        return multiply(a, b - 1, sum)


# print(multiply(5, 2))


def multiply2(a, b):
    bigger = b if a < b else a
    smaller = a if a < b else b
    return multiplyrec(smaller, bigger)


def multiplyrec(smaller, bigger, memo={}):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    elif smaller in memo:
        return memo[smaller]

    s = smaller >> 1

    side1 = multiply2(s, bigger)
    if smaller % 2 == 0:
        memo[smaller] = side1 + side1
        return memo[smaller]
    else:
        memo[smaller] = side1 + side1 + bigger
        return memo[smaller]


print(multiply2(3, 5))
