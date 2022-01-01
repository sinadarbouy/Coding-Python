def Solution(arr):
    ln = len(arr)
    return findMagic(arr, 0, ln - 1)


def findMagic(arr, start, end):
    if end < start:
        return -1

    i = int((end + start) / 2)

    if arr[i] > i:
        return findMagic(arr, start, i - 1)
    elif arr[i] < i:
        return findMagic(arr, i + 1, end)
    else:
        return i


array = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]


print(Solution(array))
