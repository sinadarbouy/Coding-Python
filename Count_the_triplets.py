
# Given an array of distinct integers.
#  The task is to count all the triplets such that sum of two elements equals the third element.


class Solution:
    def countTriplet_V3(self, arr, n):
        arr.sort()
        j = 0
        k = 0
        c = 0
        for i in range(n-2):
            j = i+1
            k = j+1
            while(k < n):
                print('i = {} and j ={} and k = {}'.format(i, j, k))
                if(arr[i]+arr[j] == arr[k]):
                    c += 1
                    j += 1
                elif(arr[i]+arr[j] < arr[k]):
                    j += 1
                    k -= 1
                k += 1
        return c

    def countTriplet_V1(self, arr, n):
        if(n == [0, 1]):
            return 0
        arr.sort()
        print(arr)
        count = 0
        for i in range(n):
            if(i == n-1):
                break
            for j in range(i+1, n):
                for k in range(j + 1, n):
                    if(arr[i] + arr[j] > arr[k]):
                        break
                    if arr[i] + arr[j] == arr[k]:
                        count = count + 1
        return count

    def countTriplet_V2(self, arr, n):
        if(n == [0, 1]):
            return 0
        count = 0
        for i in range(n):  # 0,1,2,3
            if(i == n-1):
                break
            for j in range(i+1, n):
                if(arr[i] + arr[j] in arr):
                    count += 1
        return count


n = 7
arr = [12, 8, 2, 11, 5, 14, 10]

s = Solution()

print(s.countTriplet_V3(arr, n))
