class Solution:
    def MissingNumber2(self, array, n):
        expected_sum = int((n * (n + 1)) / 2)
        return expected_sum - sum(array)

    def MissingNumber(self, array, n):
        array.sort()
        for i in range(n - 1):
            if array[i] != i + 1:
                return i + 1
        return n


s = Solution()
array = [1, 2, 3, 4]
n = 5

array2 = [6, 1, 2, 8, 3, 4, 7, 10, 5]
n2 = 10

array2 = [6, 1, 2, 8, 3, 4, 7, 10, 5]
n2 = 10

array3 = [1]
n3 = 1
print(s.MissingNumber2(array=array3, n=n3))
