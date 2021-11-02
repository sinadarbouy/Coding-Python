# Given an unsorted array A of size N that contains only non-negative integers,
#  find a continuous sub-array which adds to a given number S.

# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4

# Hash
def subArraySum(arr, n, s):
    dict1 = {}
    curr_sum = 0
    for i in range(n):
        curr_sum = curr_sum + arr[i]
        if curr_sum == s:
            return [1, i + 1]
        if curr_sum - s in dict1:
            return [dict1[curr_sum - s] + 2, i + 1]
        dict1[curr_sum] = i
    return [-1]


# Third attempt:
def subArraySum3(arr, n, s):
    startIndex = 0
    sum = 0
    i = 0
    while True:
        if startIndex > n:
            return [-1]
        sumIndex = startIndex + i
        if sumIndex >= n:
            i = 0
            startIndex += 1
            sum = 0
            sumIndex = 0
            break
        print(str(sumIndex))
        sum += arr[sumIndex]
        if sum == s:
            return [startIndex + 1, sumIndex + 1]
        elif sum > s:
            i = 0
            startIndex += 1
            sum = 0
            sumIndex = 0
        else:
            i += 1
    return [-1]


# Second attempt:
def subArraySum1(arr, n, s):
    i = 0
    while i < n:
        sum = arr[i]
        j = i + 1
        while sum < s and j < n:
            sum = sum + arr[j]
            j += 1
        if sum == s:
            return [i + 1, j]
        else:
            i = i + 1
    return [-1]


# First attempt:


def subArraySum2(arr, n, s):
    for i in range(n):
        sum = 0
        startIndex = i + 1
        for j in range(i, n):
            sum = sum + arr[j]
            if sum == s:
                endIndex = j + 1
                return [startIndex, endIndex]
            elif sum > s:
                break
            else:
                pass
    return [-1]


N = 5
S = 12
A = [1, 2, 3, 7, 5]
print(subArraySum(A, N, S))
