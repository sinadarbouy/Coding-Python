from typing import Dict


def Solution(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return Solution(n - 1) + Solution(n - 2) + Solution(n - 3)


def countWays(n):
    memo = {0: 1}
    return Solution2(n, memo)


def Solution2(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = (
            Solution2(n - 1, memo) + Solution2(n - 2, memo) + Solution2(n - 3, memo)
        )
    return memo[n]


print(countWays(37))
